from conc_lessons.utils.ansi import ln

if __name__ == "__main__":
    from conc_lessons.lesson001.teory import concurrency_teory
    from conc_lessons.utils.ansi import write

    for blk in concurrency_teory:
        write(blk.strip().replace("__L__", ""))
        ln()
