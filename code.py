from graphics import *

# Apply colors for the rectangles
results_colors = {'Progress': 'lightgreen', 'Trailer': 'lightblue', 'Retriever': 'lightyellow', 'Excluded': 'lightpink'}

def display_histogram(results, progression_data):
    #Draw Histogram
    win = GraphWin("Histogram", 400, 300)
    win.setBackground("ash")

    # Main topic
    topic_text = Text(Point(190, 20), 'Histogram Results')
    topic_text.setSize(12)
    topic_text.setStyle("bold")
    topic_text.draw(win)

    x = 50
    width = 60
    space_between = 20
    totalcount = 0  # Initialize total count

    for outcome, count in results.items():
        # Draw Rectangles
        rect = Rectangle(Point(x, 250 - count * 10), Point(x + width, 250))
        rect.setFill(results_colors[outcome])
        rect.draw(win)

        # Display topics for the rectangles
        label = Text(Point(x + width / 2, 250 + space_between), outcome)
        label.setStyle("bold")
        label.draw(win)

        # Underline the total graph
        underline = Line(Point(50,250),Point(350,250))
        underline.setWidth(1)
        underline.draw(win)

        # Display count on top of the bar
        count_text = Text(Point(x + width / 2, 250 - count * 10 - 10), str(count)) 
        count_text.setSize(8)
        count_text.draw(win)

        # Update the starting x of the rectangle
        x += width + space_between
        # Update total count
        totalcount += count 

    # Display the total value at the bottom of the graph
    totalcount = sum(results.values())
    total_text = Text(Point(190, 290), f"Total outcomes: {totalcount}")
    total_text.setSize(10)
    total_text.setStyle("bold")
    total_text.draw(win)

    # Wait for click before closing
    win.getMouse()  
    win.close()

    # Print progression data in the desired format
    print_progression_data(progression_data)

def print_progression_data(progression_data):
    print("Part 2:")
    for data in progression_data:
        pass_credits, defer_credits, fail_credits = data
        if pass_credits == 120:
            print(f"Progress - {pass_credits}, {defer_credits}, {fail_credits}")
        elif pass_credits == 100:
            print(f"Progress (module trailer) - {pass_credits}, {defer_credits}, {fail_credits}")
        elif pass_credits in [80, 60, 40, 20, 0] and fail_credits in [0, 20, 40, 60]:
            print(f"Module retriever - {pass_credits}, {defer_credits}, {fail_credits}")
        else:
            print(f"Exclude - {pass_credits}, {defer_credits}, {fail_credits}")


# Save data to a text file
def save_to_file(progression_data, filename="progression_data.txt"):
    with open(filename, 'w') as file:
        for data in progression_data:
            file.write(','.join(map(str, data)) + '\n')


def predict_progression_student():
    progression_data = []

    while True:
        try:
            pass_credits_input = input("Please enter your credits at PASS: ")

            if pass_credits_input.lower() == 'q':
                break

            pass_credits = int(pass_credits_input)

            if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue

            defer_credits = int(input("Please enter your credits at DEFER: "))
            if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue

            fail_credits = int(input("Please enter your credits at FAIL: "))
            if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range.")
                continue

            if pass_credits + defer_credits + fail_credits != 120:
                print("Total incorrect.")
            elif pass_credits == 120:
                print("Progress")
            elif pass_credits == 100:
                print("Progress (module trailer)")
            elif pass_credits in [80, 60, 40, 20, 0] and fail_credits in [0, 20, 40, 60]:
                print("Do not progress - module retriever")
            else:
                print("Exclude")

            progression_data.append((pass_credits, defer_credits, fail_credits))  # Store progression data

            while True:
                another_dataset = input("Would you like to enter another set of data?\n"
                                        "Enter 'y' for yes or 'q' to quit: ")
                if another_dataset.lower() in {'y', 'q'}:
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'q'.")

            if another_dataset.lower() == 'q':
                break

        except ValueError:
            print("Integer required")

    # Print progression data in the desired format
    print_progression_data(progression_data)

def main():
    while True:
        user_type = input("Are you a student or a mentor? If you are a student please enter 's' or if you are a mentor please enter 'm': ")
        if user_type.lower() in {'s', 'm'}:
                break
        else:
            print("Invalid input. Please enter 's' or 'm'.")
            
    if user_type.lower() == 's':
        predict_progression_student()

    elif user_type.lower() == 'm':
        results = {'Progress': 0, 'Trailer': 0, 'Retriever': 0, 'Excluded': 0}
        progression_data = []

        while True:
            try:
                pass_credits = int(input("Please enter student's credits at PASS: "))
                if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
                    print("Out of range.")
                    continue

                defer_credits = int(input("Please enter student's credits at DEFER: "))
                if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                    print("Out of range.")
                    continue

                fail_credits = int(input("Please enter student's credits at FAIL: "))
                if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                    print("Out of range.")
                    continue

                if pass_credits + defer_credits + fail_credits != 120:
                    print("Total incorrect.")
                elif pass_credits == 120:
                    print("Progress")
                    results['Progress'] += 1
                elif pass_credits == 100:
                    print("Progress (module trailer)")
                    results['Trailer'] += 1
                elif pass_credits in [80, 60, 40, 20, 0] and fail_credits in [0, 20, 40, 60]:
                    print("Do not progress - module retriever")
                    results['Retriever'] += 1
                else:
                    print("Exclude")
                    results['Excluded'] += 1

                progression_data.append((pass_credits, defer_credits, fail_credits))  # Store progression data

                while True:
                    another_student = input("Would you like to enter another student's data?\n"
                                            "Enter 'y' for yes or 'q' to quit and view results: ")
                    if another_student.lower() in {'y', 'q'}:
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'q'.")

                if another_student.lower() == 'q':
                    break

            except ValueError:
                print("Integer required")

        # Display histogram and print progression data in the desired format
        display_histogram(results, progression_data)

if _name_ == "_main_":
    main()