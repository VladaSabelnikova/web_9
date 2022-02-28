def main():
    all_collaborators = {}
    global_init(input())
    session = create_session()

    for department in session.query(Department).filter(Department.id == 1):
        members = [int(elem) for elem in department.members.split(', ')]
        for user_id in members:  # все участники department
            for job in session.query(Jobs):
                if user_id not in map(int, job.collaborators.split(', ')):
                    continue
                for user in session.query(User).filter(User.id == user_id):
                    name = f'{user.surname} {user.name}'
                    all_collaborators[name] = all_collaborators.get(name, 0)
                    all_collaborators[name] += job.work_size

    suitable_colaborators = []
    for elem, hours in sorted(all_collaborators.items(), key=lambda s: -s[1]):
        if hours > 25:
            suitable_colaborators.append(elem)
    print('\n'.join(suitable_colaborators))


if __name__ == '__main__':
    main()
