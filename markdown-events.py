import numpy as np
from glob import glob
from os import path
from datetime import datetime
import argparse


def get_events(search_str, file_path):
    """
    Return lines from vimwiki files that contain search_str.
    """
    files = glob(file_path)
    events = []
    for fname in files:
        with open(fname, 'r') as filer:
            for line in filer:
                if line == '##SKIP':
                    break
                if search_str in line and '[X]' not in line:
                    events.append(line.replace('\n', ''))

    return events


def validate_date(date):
    """
    Check that date is a valid ISO date.
    """
    try:
        datetime.fromisoformat(date)
    except ValueError:
        return False
    return True


def sort_events(events, search_str):
    """
    Sort events into date order.
    """
    dates = []
    for event in events:
        date = event.split(search_str)[-1]
        assert(validate_date(date)), f'Invalid date formatter: {date}'
        dates.append(date)

    sort_indices = np.argsort(dates)
    sort_events = np.asarray(events)[sort_indices]
    return sort_events


def print_events(events, search_str, now):
    """
    Print event list.
    """
    padding = 75
    assert(padding > 20)
    for event in events:
        event = event.replace('- [ ]', '')
        event = event.split(search_str)
        if event[1] > now:
            padder = '-'
        elif event[1] == now:
            padder = '~'
        else:
            padder = '!'
        print(event[0][:padding - 10].ljust(padding, padder) + ' ' + event[1])


def sort_and_print(search_str, file_path):
    now = str(datetime.now().strftime('%Y-%m-%d %H:%M'))
    events = get_events(search_str, file_path)
    events = sort_events(events, search_str)
    print_events(events, search_str, now)


def add_to_inbox(inbox_path):
    input_str = input('Enter input:')

    with open(inbox_path, 'a') as inbox:
        inbox.write('- [ ] ')
        inbox.write(input_str)
        inbox.write('\n')


def print_number_in_inbox(inbox_path):
    count = 0
    with open(inbox_path, 'r') as inbox:
        for line in inbox:
            if line.strip():
                count += 1

    print(count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', help='Select mode for event selection.')
    args = parser.parse_args()

    file_path = path.expanduser('~/vimwiki/gtd/*.md')
    inbox_path = path.expanduser('~/vimwiki/gtd/inbox.md')

    if args.mode == 's':
        sort_and_print('SCHEDULED:', file_path)
    elif args.mode == 'd':
        sort_and_print('DEADLINE:', file_path)
    elif args.mode == 'i':
        add_to_inbox(inbox_path)
    elif args.mode == 'c':
        print_number_in_inbox(inbox_path)
    else:
        raise RuntimeError(f'Undefined mode: {args.mode}')
