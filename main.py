from pyscript import display, document

def intrams(e):
    document.getElementById('output').innerHTML = ' '
    medcert = document.querySelector('input[name="body"]:checked').value
    registration = document.querySelector('input[name="regis"]:checked').value
    section = document.getElementById('section').value

    if medcert == 'not' and registration == 'no':
        display(f'Complete the requirements.', target="output")
    elif medcert == 'not' and registration == 'yes':
        display(f'Obtain a cleared medical certificate.', target='output')
    elif medcert == 'cleared' and registration == 'no':
        display(f'Complete the requirements.', target='output')
    elif registration == 'yes' and medcert == 'cleared' and section == 'emerald':
        display(f'You are in Blue Bears!', target='output')
    elif registration == 'yes' and medcert == 'cleared' and section == 'ruby':
        display(f'You are in Yellow Hornets!', target='output')
    elif registration == 'yes' and medcert == 'cleared' and section == 'sapphire':
        display(f'You are in Red Bulldogs!', target='output')
    elif registration == 'yes' and medcert == 'cleared' and section == 'topaz':
        display(f'You are in Green Hornets!', target='output')
    else:
        display(f'Invalid.', target='output')
