from src.job_scheduler import JobScheduler


def display_jobs(scheduler):
    print("\n==================== JOB SCHEDULER =========================")
    print(f"Detyrat ne pritje: {scheduler.pending_jobs()}")

    if scheduler.is_empty():
        print("Ska Detyre ne Pritje.")
    else:
        print("Detyrat po presin per processimin e tyre.")


def main():
    scheduler = JobScheduler()

    print("=" * 60)
    print("======================-----NEXUS-----=======================")
    print("=" * 60)

    
    print("\n[1] SHTIMI I PUNEVE/DETYRAVE")

    jobs = [
        ("Database Backup", 3, "Scheduled database backup"),
        ("Security Alert", 1, "Critical security notification"),
        ("Generate Report", 2, "Generate monthly report"),
        ("Server Failure", 1, "Server availability issue"),
        ("System Update", 4, "Routine system maintenance"),
    ]

    for name, priority, description in jobs:
        job = scheduler.add_job(name, priority, description)

        print(
            f"Pune E Shtuar #{job.job_id}: "
            f"{job.name} | Prioriteti: {job.priority}"
        )
    print(" ")
    print("=" * 60)

    print("\n[2] GJENDJA E PLANIFIKUESIT")
    display_jobs(scheduler)

    print("\n[3] PERPUNIMI I DETYRAVE")
    print("-" * 60)

    while not scheduler.is_empty():
        job = scheduler.process_next()

        print(
            f"Detyra E Procesuar #{job.job_id}: "
            f"{job.name} | Prioriteti: {job.priority}"
        )
    print(" ")
    print("=" * 60)
    print("\n[4] HISTORIA E EKZEKUTIMEVE")
    print("-" * 60)

    for index, job in enumerate(
        scheduler.execution_history(), start=1
    ):
        print(
            f"{index}. {job.name} "
            f"(Prioriteti: {job.priority})"
        )
    print(" ")
    print("=" * 60)
    print("\n[5] GJENDJA PERFUNDIMTARE ")
    print(f"Detyrat Ne Pritje: {scheduler.pending_jobs()}")
    print(f"Detyrat E Perpunuara: {len(scheduler.execution_history())}")
    print(f"Planifikuesi Eshte Bosh: {scheduler.is_empty()}")

    print("\n" + "=" * 60)
    print("===========---- PLANIFIKIMI PERFUNDOI ----==================")
    print("=" * 60)


if __name__ == "__main__":
    main()