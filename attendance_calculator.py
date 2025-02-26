def flexible_attendance_calculator():
    """Interactive function allowing users to input any 2 of (present, absent,)"""

    total_classes = present_classes = absent_classes = None

    print("\n--- Attendance Calculator ---")
    print("You can enter ANY 2 of the following:\n- Classes Present\n- Classes Absent\n- Total Classes\n")

    while True:
        try:
            # Input
            present_input = input("Enter Classes Present: ").strip()
            absent_input = input("Enter Classes Absent: ").strip()
            total_input = input("Enter Total Classes: ").strip()

            # Inputs to integers
            total_classes = int(total_input) if total_input else None
            present_classes = int(present_input) if present_input else None
            absent_classes = int(absent_input) if absent_input else None

            # 3rd value finder
            if total_classes is None and present_classes is not None and absent_classes is not None:
                total_classes = present_classes + absent_classes
            elif present_classes is None and total_classes is not None and absent_classes is not None:
                present_classes = total_classes - absent_classes
            elif absent_classes is None and total_classes is not None and present_classes is not None:
                absent_classes = total_classes - present_classes

            # validate attendanve (present, absent)
            if None in [total_classes, present_classes, absent_classes]:
                print("⚠️ Please enter at least 2 values! Try again.")
                continue

            if present_classes > total_classes or present_classes < 0 or absent_classes < 0:
                print("❌ Invalid input! Ensure Present ≤ Total and no negative values.")
                continue

            break

        except ValueError:
            print("❌ Invalid input! Please enter numerical values only.")

    # Basic Calculations
    while True:
        try:
            required_attendance = float(input("Enter the minimum required attendance percentage: "))
            if 0 <= required_attendance <= 100:
                break
            else:
                print("⚠️ Invalid percentage! Enter a value between 0 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid percentage.")

    # Compute attendance percentage
    attendance_percentage = (present_classes / total_classes) * 100

    # Required Attendance Calculator
    needed_classes = None
    if attendance_percentage < required_attendance:
        needed_classes = 0
        new_total, new_present = total_classes, present_classes

        while (new_present / new_total) * 100 < required_attendance:
            needed_classes += 1
            new_total += 1
            new_present += 1

    # Skippable Classes
    max_skippable_classes = 0
    if attendance_percentage > required_attendance:
        new_present = present_classes
        while new_present > 0 and (new_present / (total_classes + max_skippable_classes)) * 100 > required_attendance:
            max_skippable_classes += 1
            new_present -= 1

        max_skippable_classes -= 1

    # Target Attendance
    while True:
        try:
            target_attendance = float(input("Enter your target attendance percentage: "))
            if 0 <= target_attendance <= 100:
                break
            else:
                print("⚠️ Invalid percentage! Enter a value between 0 and 100.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid percentage.")

    extra_needed_classes = None
    if target_attendance > attendance_percentage:
        extra_needed_classes = 0
        new_total, new_present = total_classes, present_classes

        while (new_present / new_total) * 100 < target_attendance:
            extra_needed_classes += 1
            new_total += 1
            new_present += 1

    # Results Display
    print("\n--- Attendance Summary ---")
    print(f"📌 Total Classes: {total_classes}")
    print(f"✔️ Classes Attended: {present_classes}")
    print(f"❌ Classes Missed: {absent_classes}")
    print(f"✅ Current Attendance: {attendance_percentage:.2f}%")
    print(f"🎯 Required Attendance: {required_attendance}%")

    if needed_classes is not None:
        print(f"⚠️ You need to attend at least {needed_classes} more classes to reach {required_attendance}% attendance.")
    else:
        print(f"🎉 Your attendance is already above {required_attendance}%.")

    if max_skippable_classes > 0:
        print(f"🛑 You can skip up to {max_skippable_classes} more classes and still stay above {required_attendance}%.")
    else:
        print(f"⚠️ Skipping any more classes will drop you below {required_attendance}%.")

    if extra_needed_classes is not None:
        print(f"🎯 To reach {target_attendance}%, you need to attend at least {extra_needed_classes} more classes without missing any.")

    # Predictions
    print("\n🔮 Would you like to see attendance predictions? (Yes/No)")
    choice = input("Enter your choice: ").strip().lower()

    if choice in ["yes", "y"]:
        while True:
            try:
                skip_more = int(input("\nEnter number of extra classes you might skip: "))
                if skip_more >= 0:
                    new_attendance_skip = ((present_classes) / (total_classes + skip_more)) * 100
                    print(f"⚠️ If you skip {skip_more} more classes, your attendance will be: {new_attendance_skip:.2f}%")
                else:
                    print("❌ Enter a valid positive number.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

            try:
                attend_more = int(input("\nEnter number of extra classes you might attend: "))
                if attend_more >= 0:
                    new_attendance_attend = ((present_classes + attend_more) / (total_classes + attend_more)) * 100
                    print(f"✅ If you attend {attend_more} more classes, your attendance will be: {new_attendance_attend:.2f}%")
                else:
                    print("❌ Enter a valid positive number.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

            break

    print("\n--- End of Report ---")

flexible_attendance_calculator()