# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Heinz")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room:
        zoom 4.3

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "heinz.png" to the images
    # directory.

    show heinz smile hand1 arm1:
        zoom 0.6
        xalign 0.5
        yalign 1.0

    # These display lines of dialogue.

    h "Hi there! I'm Heinz. I'm your principle!"

    show heinz smile eye:
        zoom 0.6
        xalign 0.5
        yalign 1.0

    h "Here at Apopka High, we welcome all. You can choose which uniform you'd like to wear and what you want to do. We have many courses as well."

    show heinz smile arm2:
        zoom 0.6
        xalign 0.5
        yalign 1.0

    h "Please let me know if you need anything."

    h "i fucking hate hackatime this is pissing me OFF."

    # This ends the game.

    return