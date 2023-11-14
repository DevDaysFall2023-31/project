import argparse
import asyncio
import time
import aiohttp
import logging
import random
import string
import yandex_music

from aiolimiter import AsyncLimiter


def get_random_son_id() -> str:
    client: yandex_music.Client = yandex_music.Client().init()
    search_result: yandex_music.Search = client.search(random.choice(string.ascii_letters))
    return search_result.best.result.id


def construct_url(args):
    if args.action == "favourites":
        return f"http://{args.ip}:{args.port}/tracks/favourites"
    elif args.action == "similar":
        return f"http://{args.ip}:{args.port}/tracks/{get_random_son_id()}/similar"
    elif args.action == "peak":
        return f"http://{args.ip}:{args.port}/peaks/{get_random_son_id()}"
    else:
        return None


async def runner(args):
    throttler: AsyncLimiter = AsyncLimiter(max_rate=float(args.rps), time_period=1.0)
    tasks: list = []
    succeed: int = 0
    total: int = 0
    time_spent: float = 0
    url: str = construct_url(args)

    async with aiohttp.ClientSession() as session:
        try:
            start_time: float = time.time()

            while total < int(args.rps) * int(args.seconds):
                async with throttler:
                    tasks.append(asyncio.create_task(session.get(url)))
                    total += 1
            responses = await asyncio.gather(*tasks)

            time_spent = time.time() - start_time
            for reponse in responses:
                if reponse.status == 200:
                    succeed += 1
        except Exception as e:
            logging.error("Exception during requests sending was thrown: %s", str(e))
    
    logging.info("Total number of requests: %s", total)
    logging.info("Number of succeed requests: %s", succeed)
    logging.info("Total time spent: %s [seconds]", time_spent)
                    

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog='Load testing script',
        description=(
            'Sends requests to to service'
        )
    )

    parser.add_argument(
        '-a',
        '--action',
        help='Possible values are: "favourites", "similar", "peak"'
    )
    parser.add_argument(
        '-r',
        '--rps',
        default=10
    )
    parser.add_argument(
        '-s',
        '--seconds',
        default=5
    )
    parser.add_argument(
        '-ip',
        '--ip',
        default="127.0.0.1"
    )
    parser.add_argument(
        '-p',
        '--port',
        default="80"
    )
    args = parser.parse_args()
    
    try:
        asyncio.run(runner(args))
    except Exception as e:
        logging.error("Exception was thrown: %s", str(e))
    