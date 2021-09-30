import argparse
import time

DEFULT_WORK_MINUTES = 25
DEFULT_BREAK_MINUTES = 5


def parse_params():
    name = 'tomato.py'
    parse = argparse.ArgumentParser(prog=name, usage=f'{name} [options]', description='tomato worker, Ctrl+C to exit')
    parse.add_argument(
        '-t', '--tomato', type=int, default=DEFULT_WORK_MINUTES, help=f'start a {DEFULT_WORK_MINUTES} minutes tomato clock'
    )
    parse.add_argument(
        '-r', '--rest', type=int, default=DEFULT_BREAK_MINUTES, help=f'Began to rest for {DEFULT_BREAK_MINUTES} minutes'
    )
    args = parse.parse_args()
    return args.tomato, args.rest


def tomato_worker():
    minutes, rest = parse_params()
    print(f'>>>tomato worker：start a {minutes} 🍅 minutes and rest a {rest} ♨️  minutes')
    start_time = time.perf_counter()
    while True:
        diff_seconds = int(round(time.perf_counter() - start_time))
        left_seconds = minutes * 60 - diff_seconds
        if left_seconds <= 0:
            print('\n🎉😄🎆 congratulations to you become tomato worker')
            break

        count_down = '{}:{} ⏰'.format(int(left_seconds / 60), int(left_seconds % 60))
        console_progress_bar(diff_seconds, minutes, count_down)
        time.sleep(1)


def console_progress_bar(diff_seconds, minutes, extra=''):
    frac = diff_seconds / (minutes * 60)
    filled = round(frac * minutes)
    print('\r', '🍅' * filled + '--' * (minutes - filled), '[{:.0%}]'.format(frac), extra, end='')


def notify():
    pass


if __name__ == '__main__':
    try:
        tomato_worker()
    except KeyboardInterrupt:
        print('\n 👋 goodbye~')
    except Exception as e:
        print(e)
        exit(1)
