#!/bin/bash

tarot=(
    "The Fool"
    "The Magician"
    "The High Priestess"
    "The Empress"
    "The Emperor"
    "The Hierophant"
    "The Lovers"
    "The Chariot"
    "Strength"
    "The Hermit"
    "The Wheel of Fortune"
    "Justice"
    "The Hanged Man"
    "Death"
    "Temperance"
    "The Devil"
    "The Tower"
    "The Star"
    "The Moon"
    "The Sun"
    "Judgement"
    "The World"
)

random_index=$((RANDOM % ${#tarot[@]}))
random_card=${tarot[random_index]}
echo "$random_card"