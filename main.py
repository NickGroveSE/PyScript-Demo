import js

def main():
    print("running")

def click():
    new_div = js.document.createElement("div")
    diagram_space = js.document.getElementById("diagram-space")

    new_div.style.width = "100px"
    new_div.style.height = "100px"
    new_div.style.backgroundColor = "yellow"
    diagram_space.appendChild(new_div)

    print('click')

if __name__ == "__main__":
    main()



