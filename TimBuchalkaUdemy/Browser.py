import webbrowser

# webbrowser.open("https://www.python.org/")
import behave

chrome = webbrowser.get(using='chrome')
chrome.open_new_tab("http://www.python.org/")
for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=";", end=" ")
help(behave.Step(), "")
