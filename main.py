from threading import Thread, active_count

from eth_account import Account


def generate_and_check() -> None:
    account = Account.create()

    if prefix:
        if not account.address.startswith(prefix):
            return

    if suffix:
        if not account.address.endswith(suffix):
            return

    print(f'Address: {account.address}\n'
          f'Private Key: {account.key.hex()}')

    with open(file='founded.txt', mode='a', encoding='utf-8-sig') as file:
        file.write(f'{account.address}:{account.key.hex()}\n')


if __name__ == '__main__':
    threads: int = int(input('Threads: ')) + 1
    prefix: str = input('Prefix (to skip press Enter): ')
    suffix: str = input('Suffix (to skip press Enter): ')

    print('Generating addresses...\n')

    while True:
        if active_count() < threads:
            Thread(target=generate_and_check).start()
