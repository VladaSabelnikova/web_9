def main():
    global_init(input())
    session = create_session()

    for job in session.query(Jobs).filter(
        Jobs.work_size < 20,
        Jobs.is_finished == 0
    ):
        print(f'<Job> {job.job}')


if __name__ == '__main__':
    main()
