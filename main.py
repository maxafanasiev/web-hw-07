import argparse
from managers import TeachersManager, StudentsManager, SubjectsManager, GroupsManager, GradesManager


def create_manager(model):
    match model:
        case "Teacher":
            return TeachersManager()
        case "Student":
            return StudentsManager()
        case "Grade":
            return GradesManager()
        case "Subject":
            return SubjectsManager()
        case "Group":
            return GroupsManager()


def main():
    managers = {
        "Teacher": create_manager("Teacher"),
        "Group": create_manager("Group"),
        "Student": create_manager("Student"),
        "Subject": create_manager("Subject"),
        "Grade": create_manager("Grade"),

    }

    parser = argparse.ArgumentParser(description="CLI Application for CRUD operations with the database.")
    parser.add_argument("--action", "-a", choices=["create", "list", "update", "remove"], required=True,
                        help="Action to perform: create, list, update, or remove.")
    parser.add_argument("--model", "-m", choices=list(managers.keys()), required=True,
                        help="Model on which to perform the action.")
    parser.add_argument("--id", type=int, help="ID of the record to update or remove.")
    parser.add_argument("--name", "-n", help="Name for the new record or updated record.")
    parser.add_argument("--group_id", type=int, help="Group ID for Student creation.")
    parser.add_argument("--subject_id", type=int, help="Subject ID for Grade creation.")
    parser.add_argument("--student_id", type=int, help="Student ID for Grade creation.")
    parser.add_argument("--grade", type=int, help="Grade value for Grade creation.")
    parser.add_argument("--teacher_id", type=int, help="Teacher ID for Subject creation.")

    args = parser.parse_args()

    print(args.action)

    if args.model not in managers:
        print(f"Invalid model: {args.model}. Available models: {', '.join(managers.keys())}")
        return
    manager = managers[args.model]

    if args.action == "create":
        manager.create(args)
    elif args.action == "list":
        manager.list()
    elif args.action == "update" and args.id and args.name:
        manager.update(args)
    elif args.action == "remove" and args.id:
        manager.remove(args.id)
    else:
        print("Invalid command or missing arguments. Please check the usage.")


if __name__ == "__main__":
    main()
