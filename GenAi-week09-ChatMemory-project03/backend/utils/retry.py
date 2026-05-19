import time

def retry_function(
    func,
    retries=3,
    delay=2
):

    for attempt in range(retries):

        try:

            return func()

        except Exception as e:

            print(
                f"Retry {attempt+1} failed: {e}"
            )

            time.sleep(delay)

    raise Exception(
        "Max retries exceeded"
    )