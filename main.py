# Finding Surnames

from pyscript import display, document

def name_finder(e):
    document.getElementById('result').innerHTML = ' '
    last_name = document.getElementById('surname').value.capitalize().strip()
    first_name = document.getElementById('fname').value.capitalize().strip()

    cocc_members_fname = ['Zoe', 'Aiva', 'Maryam', 'Zarina', 'Hans', 'Nathan']
    cocc_members_lastname = ['Reyes', 'Suson', 'Ledesma', 'Perez', 'Baquiran', 'Bautista']
    student_checker = (first_name in cocc_members_fname and last_name in cocc_members_lastname)
    display_message = (f'Sorry {first_name} {last_name}, your name is not on the list.', f'Congratulations {first_name} {last_name}! You are now part of the COCC Club.')

    display(display_message[student_checker], target='result')