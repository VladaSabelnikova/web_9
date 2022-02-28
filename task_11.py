def main():
    max_n_colaborators = 0
    all_team_leaders = []

    global_init(input())
    session = create_session()

    for job in session.query(Jobs):
        for user in session.query(User).filter(User.id == job.team_leader):
            n_colaborators = len((job.collaborators).split(', '))
            max_n_colaborators = max(max_n_colaborators, n_colaborators)

            all_team_leaders.append(
                [f'{user.surname} {user.name}', n_colaborators]
            )

    all_team_leaders.sort(key=lambda s: -s[1])
    max_team_leaders = []
    for team_leader, n in all_team_leaders:
        if n != max_n_colaborators:
            break
        max_team_leaders.append(team_leader)
    print('\n'.join(set(max_team_leaders)))


if __name__ == '__main__':
    main()
