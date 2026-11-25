# NEXUS - Algoritem Analize


## 1. MinHeap 

Min Heap eshte nje strukture e te dhenave binary bazuar ne peme (binary tree-based DS)  e cila eshte e implementuar duke perdorur lista te Python (scripts) 

Elementi me i vogel gjithmon ruhet ne root . 

Kurse operacionet qe jane te perdorura ne MinHeap dhe Kompleksiteti kohor i tyre >

| Operacioni  | Kompleksiteti Kohor |
|-------------|---------------------|
| Insert      |      O(log n)       |
| Extract Min |      O(log n)       | 
| Peek        |        O(1)         |
| Heapify     |        O(n)         |
| Validate    |        O(n)         | 
| Size        |        O(1)         |
| Is Empty    |        O(1)         |


### Heap Construction 

Operacioni i Heapify perdor bottom-up (nga poshte larte) kontruktorin e heap algoritmitt

Fillon prej nyjes(node) qe eshte pa gjethe (non-leaf) dhe e zhvendos posht derisa te jet root e arritshme. 

Kompleksiteti kohor eshte O(n) 


## 2. PriorityQueue

PriorityQ perdor MinHeap qe ti organizoj elementet duke u bazuar ne prioritetin e tyre (pra eshte mbi MinHeap).

Ne baz te Operacionit dhe Kompleksitetit Kohor : 

| Operacioni  | Kompleksiteti Kohor |
|-------------|---------------------|
| Enqueue     |      O(log n)       |
| Dequeue     |      O(log n)       | 
| Peek        |        O(1)         |
| Size        |        O(1)         |

Numri rendor ka renditjen FIFO (First-in-First-out), pra elementet me prioritetin e njejte perpunohen sipas rendit te shtimit. 

### 3. JobScheduler

JobScheduler perdor PriorityQueue per me menagju dhe procesu punet/detyrat e planifikuara.


| Operacioni   | Kompleksiteti Kohor |
|--------------|---------------------|
| Add Job      |      O(log n)       |
| Process Next |      O(log n)*      | 
| Cancel Job   |    O(1) average     |
| Pending Jobs |        O(1)         |
{ Execution    }	                 |
{ History      }	    O(n)         |

Punet e anuluara trajtohen duke peredorur lazy deletion(fshirje te vonuar). 
Ato anashkalohen kur arrijne perpara tek PriorityQueue.

Process Next eshte e theksuar me * , arsyeja eshte se ne nje detyre normale kompleksiteti kohore eshte siq shihet ne tabel (pra O(logn)) por nese ka disa detyra te anuluara ne fillim te radhes, mund te largoj nje nga nje derisa te gjej detyren aktive. Pra per k detyra te anuluara kompleksiteti kohor mund te jete "O((k+1)log n)"