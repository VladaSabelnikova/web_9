def main():
    global_init(input())
    session = create_session()

    for user in session.query(User).filter(User.age < 18):
        print(f'{user} {user.age} years')


if __name__ == '__main__':
    main()
