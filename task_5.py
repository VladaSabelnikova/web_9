def main():
    global_init(input())
    session = create_session()

    for user in session.query(User).filter(User.address == 'module_1'):
        print(user)


if __name__ == '__main__':
    main()
