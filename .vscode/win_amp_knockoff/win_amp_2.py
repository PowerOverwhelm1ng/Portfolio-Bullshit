from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QAbstractListModel, QListView, QStyle
from PyQt5.QtCore import QUrl, Qt, QMimeData, QAbstractListModel, QItemSelectionModel, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist
from PyQt5.QtGui import QPalette, QColor




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUI(self)

        self.player = QMediaPlayer()
        self.player.error.connect(self.erroralert)

        #COnnect control buttons and slides for media player
        self.playButton.pressed.connect(self.player.play)
        self.pauseButton.pressed.connect(self.player.pause)
        self.stopButton.pressed.connect(self.player.stop)

        #vol COntrol

        self.volumeSlider.valueChanged.connect(self.player.setVolume)
        self.timeSlider.valueChanged.connect(self.player.setPosition)
        #update the display as play pos changes
        self.player.durationChanged.connect(self.update_duration)
        self.player.positionChanged.connect(self.update_position)

        #playlist
        self.playlist = QMEdiaPlaylist()
        self.player.setPlaylist(self.playlist)
    #Control buttons
        self.previousButton.pressed.connect(self.playlist.previous)
        self.nextButton.pressed.connect(self.playlist.next)

        #display

        self.model = PlaylistModel(self.playlist)
        self.playlistView.setModel(self.model)
        self.playlist.currentIndexChanged.connect(self.playlist_positionchanged)
        selection_model = self.playlistView.selctionModel()
        selection_model.selectionChanged.connect(self.playlist_selection_changed)

        #opening and dropping
        self.open_file_action.triggered.connect(self.open_file)
        self.setAcceptDrops(True)

        #VIDEO
        self.viewer = ViewerWindow(self)
        self.viewer.setWindowsFlags(self.viewer.windowFlags()| Qt.WindowStaysOnTopHint)
        self.viewer.setMinimumSize(Qsize(480,360))

        videoWidget = QVideoWidget()
        self.viewer.setCentralWidget(videoWidget)
        self.player.setVideoOutput(videoWidget)
        #Enable toggles for viewer
        self.viewButton.toggled.connect(self.toggle_viewer)
        self.viewer.state.connect(self.viewButton.setChecked)

        #playlist model

class PlaylistModel(QAbstractListModel):
        def __init__(self, playlist, *args, **kwargs):
            super(PlaylistModel,self).__init__(*args, **kwargs)
            self.playlist = playlist

        def data(Self, index, role):
            if role == Qt.DisplayRole:
                media = self.playlist.media(index_row())
                return media.canonicalUrl().fileName()
            
        def rowCount(self, index):
            return self.playlist.mediaCount()
        
        def playlist_selection_changed(self, ix):
            # we receive a Qitemselection from selection changed
            i = ix.indexes()[0].row()
            self.playlist.setCurrentIndex(i)

            #update selection in playlist as track progresses

        def playlist_position_changed(self, i):
            if i > -1:
                ix=self.model.index(i)
                self.playListView.setCurrentIndex(ix)

        #Drag and drop operations

        def dragEnterEvent(self, e):
            if e.mimeData().hasUrls():
                e.acceptProposedAction()

        #The dropEvent iterates over the URLs in the provided data, 
        # and adds them to the playlist. If we're not playing, 
        # dropping the file triggers autoplay from the newly added file.
        # 
        def dropEvent(self,e):
            for url in e.mimeData().urls():
                self.playlist.addMedia(
                    QMediaContent(url)
                )
                self.modellayoutChanged.emit()

                #IF not playing seeking to first of newly added + play
                # 
                if self.player.state() != QMediaPlayer.PlayingState:
                    i = self.playlist.mediaCount() - len(e.mimeData().urls())
                    self.playlist.setCurrentIndex(i)      
                    self.player.play()


        def open_file(self):
            path, _ = QFileDialog.getOpenFileName(self,"Open file", "", "mp3 Audio (*.mp3);;mp4 Video (*.mp4);;Movie files (*.mov);;All files (*.*)")

            if path:
                self.playlist.addMedia(
                    QMediaContent(
                        QUrl.fromLocalFile(path)
                    )
                )

            self.model.layoutChanged.emit()

            def update_duration(self, duration):
                self.timeSlider.setMaximum(duration)

                if duration >= 0:
                    self.totalTimeLabel.setText(hhmmss(duration))

            def update_position(self, position):
                if position >= 0:
                    self.currentTimeLabel.setText(hhmmss(position))
            # Disable the events to prevent updating triggering a setPosition event (can cause stuttering).
            # 
            # 
            self.timeSlider.blockSignals(True)
            self.timeSlider.setValue(position)
            self.timeSlider.blockSignals(False)     

            def hhmmss(ms):
                # s = 1000
                # m = 6000
                # h 3600000
                s = round(ms/1000)
                m, s = divmod(s,60)
                h, m = divmod(m, 60)
                return ("%d:%02d:%02d" % (h,m,s)) if h else("%d:%02d" % (m,s))
            
class ViewerWindow(QMainWindow):
            state = pyqtSignal(bool)

            def closeEvent(self, e):
                 # Emit the window state, to update the viewer toggle button.
                 self.state.emit(False)

            def toggle_viewer(self, state):
                if state:
                    self.viewer.show()
                else:
                    self.viewer.hide()
            app.setStyle("Fusion")
            palette = QPalette() # Get a copy of the standard palette.
            palette.setColor(QPalette.Window, QColor(53, 53, 53))
            palette.setColor(QPalette.WindowText, Qt.white)
            palette.setColor(QPalette.Base, QColor(25, 25, 25))
            palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            palette.setColor(QPalette.ToolTipBase, Qt.white)
            palette.setColor(QPalette.ToolTipText, Qt.white)
            palette.setColor(QPalette.Text, Qt.white)
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, Qt.white)
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(42, 130, 218))
            palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            palette.setColor(QPalette.HighlightedText, Qt.black)
            app.setPalette(palette)

            # Additional CSS styling for tooltip elements.
            app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
