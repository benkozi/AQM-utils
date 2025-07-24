from ads.core import Context, S3SyncRunner


def test_gaeac6() -> None:
    first_cycle_date = "2023060112"
    last_cycle_date = "2023060212"
    dst_dir = "/gpfs/f6/bil-fire8/scratch/Benjamin.Koziol/tmp/aqm-use-case-download"
    ctx = Context(
        first_cycle_date=first_cycle_date,
        last_cycle_date=last_cycle_date,
        dst_dir=dst_dir,
        dry_run=True,
    )
    runner = S3SyncRunner(ctx)
    runner.run()
