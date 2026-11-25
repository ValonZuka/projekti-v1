# NEXUS – Sistem Per Planifikimin e Detyrave Bazuar ne Prioritetet e tyre 

# NEXUS - Priority-Based Job Scheduling System

## Përshkrimi i projektit

NEXUS është një sistem për menaxhimin dhe organizimin e detyrave bazuar në prioritet. Qëllimi i projektit është të demonstrojë përdorimin praktik të strukturave të të dhënave dhe algoritmeve, duke kombinuar MinHeap, Priority Queue dhe Job Scheduler në një sistem të vetëm.

Sistemi mundëson shtimin e detyrave, caktimin e prioriteteve, organizimin e tyre sipas rëndësisë, anulimin e detyrave që ende nuk janë ekzekutuar dhe ruajtjen e historikut të ekzekutimit.

Në NEXUS, detyra me numër më të vogël të prioritetit konsiderohet më e rëndësishme dhe ekzekutohet e para. Kur dy ose më shumë detyra kanë prioritet të njëjtë, sistemi ruan rendin në të cilin janë shtuar.

## Si funksionon sistemi?

NEXUS përbëhet nga tri pjesë kryesore që punojnë së bashku:

**1. MinHeap – Struktura bazë**

MinHeap është baza mbi të cilën ndërtohet sistemi. Ai implementohet duke përdorur një Array, pa pasur nevojë për krijimin e Node Objects ose Linked Lists.

Për çdo element në array përdoren këto formula për përcaktimin e pozitës së prindit dhe fëmijëve:

- Parent: `(i - 1) // 2`
- Left Child: `2 * i + 1`
- Right Child: `2 * i + 2`

MinHeap siguron që elementi me vlerën më të vogël të jetë gjithmonë në krye të strukturës.

**2. Priority Queue – Organizimi sipas prioritetit**

Priority Queue përdor MinHeap për të organizuar detyrat sipas prioritetit të tyre.

Çdo detyrë ruhet së bashku me prioritetin dhe një numër rendor. Ky numër përdoret për të ruajtur rendin e shtimit kur disa detyra kanë prioritet të njëjtë.

**3. Job Scheduler – Menaxhimi i detyrave**

Job Scheduler është pjesa që menaxhon procesin e punës. Ai komunikon me Priority Queue dhe mundëson shtimin, anulimin dhe ekzekutimin e detyrave.

Çdo detyrë merr një ID unike, emër dhe prioritet. Scheduler gjithashtu ruan historikun e detyrave të përfunduara dhe numrin e detyrave që ende presin të ekzekutohen.

## Rrjedha e funksionimit

Procesi i punës zhvillohet në këtë renditje:

1. Përdoruesi shton një detyrë dhe cakton prioritetin e saj.
2. Job Scheduler krijon detyrën dhe i cakton një ID unike.
3. Detyra dërgohet në Priority Queue.
4. Priority Queue e organizon detyrën duke përdorur MinHeap.
5. Kur kërkohet ekzekutimi, Scheduler merr detyrën me prioritetin më të lartë.
6. Detyra shënohet si e përfunduar dhe ruhet në historik.
7. Nëse një detyrë anulohet para ekzekutimit, Scheduler e përjashton atë nga procesimi.

Në rastet kur detyrat anulohen, sistemi përdor metodën Lazy Deletion. Kjo do të thotë se detyra shënohet si e anuluar dhe anashkalohet kur arrin radha e saj për procesim.

## Hierarkia e komponentëve

Komponentët janë të organizuar në këtë mënyrë:

Job Scheduler  
↓  
Priority Queue  
↓  
MinHeap  
↓  
Array Representation

MinHeap është struktura bazë, Priority Queue e përdor atë për organizimin e detyrave, ndërsa Job Scheduler qëndron në nivelin më të lartë dhe kontrollon procesin e menaxhimit dhe ekzekutimit.

## Funksionalitetet kryesore

- Shtimi i detyrave të reja.
- Caktimi i prioriteteve.
- Organizimi automatik sipas prioritetit.
- Ruajtja e rendit të shtimit për prioritete të njëjta.
- Marrja dhe ekzekutimi i detyrës me prioritetin më të lartë.
- Anulimi i detyrave që nuk janë ekzekutuar.
- Gjenerimi i ID-ve unike për detyrat.
- Ruajtja e historikut të ekzekutimit.
- Kontrollimi i numrit të detyrave në pritje.
- Testimi automatik i funksionaliteteve.

## Teknologjitë e përdorura

- Python 3.14
- Pytest
- Git dhe GitHub

## Struktura e projektit

```text
projekti-v1/
│
├── src/
│   ├── __init__.py
│   ├── min_heap.py
│   ├── priority_queue.py
│   ├── job_scheduler.py
│   ├── main.py
│   └── main_jobSch.py
│
├── tests/
│   ├── test_min_heap.py
│   ├── test_priority_queue.py
│   └── test_job_scheduler.py
│
├── docs/
│   └── algorithm_analysis.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Instalimi dhe ekzekutimi

Për ta ekzekutuar projektin lokalisht, fillimisht klonohet repository:

```bash
git clone https://github.com/ValonZuka/projekti-v1.git
cd projekti-v1
```

Krijimi dhe aktivizimi i virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instalimi i librarive të nevojshme:

```bash
python -m pip install -r requirements.txt
```

Për ekzekutimin e demonstrimit të MinHeap:

```bash
python .\src\main.py
```

Për ekzekutimin e demonstrimit të Job Scheduler:

```bash
python -m src.main_jobSch
```

## Testimi automatik

Projekti përdor Pytest për testimin e funksionaliteteve dhe verifikimin e rezultateve.

Për ekzekutimin e të gjitha testeve:

```bash
python -m pytest -v
```

Testet janë të organizuara sipas komponentëve kryesorë:

- `test_min_heap.py` – teston operacionet e MinHeap.
- `test_priority_queue.py` – teston organizimin sipas prioritetit dhe rendin e detyrave.
- `test_job_scheduler.py` – teston menaxhimin, anulimin dhe ekzekutimin e detyrave.

## Analiza e kompleksitetit

| Operacioni | Kompleksiteti |
|---|---|
| MinHeap – Insert | O(log n) |
| MinHeap – Extract Min | O(log n) |
| MinHeap – Peek | O(1) |
| MinHeap – Heapify | O(n) |
| Priority Queue – Enqueue | O(log n) |
| Priority Queue – Dequeue | O(log n) |
| Priority Queue – Peek | O(1) |
| Job Scheduler – Add Job | O(log n) |
| Job Scheduler – Cancel Job | O(1) mesatarisht |
| Job Scheduler – Pending Jobs | O(1) |

Për raste të veçanta, procesimi mund të kërkojë më shumë kohë nëse duhet të anashkalohen disa detyra të anuluara.

Për analizë më të detajuar të algoritmeve dhe kompleksitetit, shiko dokumentin `docs/algorithm_analysis.md`.

## Ndarja e punës në projekt

Projekti është zhvilluar përmes bashkëpunimit të tre anëtarëve të ekipit, ku secili ka përgjegjësi në pjesë të ndryshme të sistemit.

**Valoni – 40%**

Përgjegjës për implementimin e MinHeap duke përdorur Array Representation, zhvillimin e algoritmeve kryesore, implementimin e Job Scheduler, integrimin e komponentëve dhe testimin automatik të sistemit.

**Dea – 30%**

Përgjegjëse për zhvillimin e Frontend-it, dizajnimin e ndërfaqes së përdoruesit dhe lidhjen e saj me funksionalitetet e Backend-it. Ndërfaqja do të mundësojë shtimin dhe menaxhimin e detyrave, caktimin e prioriteteve dhe shikimin e historikut të ekzekutimit.

**Anesa – 30%**

Përgjegjëse për dokumentimin dhe testimin e Priority Queue, analizimin e funksionimit të saj në bashkëpunim me MinHeap, si dhe përgatitjen e dokumentacionit teknik dhe validimin e funksionaliteteve të projektit.
