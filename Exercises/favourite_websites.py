import webbrowser

# list your fav Links
w3schoolLink = 'https://www.w3schools.com/'


def firefox(website):
    url = ""
    if '.com' not in website:
        url = 'www.'+website+'.com'

    else:
        url = website

    webbrowser.open(url) 
