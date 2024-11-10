---
created: 2024-11-05T10:38:51 (UTC -06:00)
tags: []
source: https://uop.ucertify.com/app/?func=ebook&chapter_no=3#05jm6
author: uCertify
---

# Lesson 3 : Maps, Hash Tables, Skip Lists, Search Trees, and Sorting and Selection -uCertify

> ## Excerpt
> Don’t want to hear from us? Manage your email subscription and update your preferences. You can resubscribe anytime to stay updated on the latest IT trends.

---
In the previous section, we showed that Ω(_n_ log _n_) time is necessary, in the worst case, to sort an _n_\-element sequence with a comparison-based sorting algorithm. A natural question to ask, then, is whether there are other kinds of sorting algorithms that can be designed to run asymptotically faster than _O_(_n_ log _n_) time. Interestingly, such algorithms exist, but they require special assumptions about the input sequence to be sorted. Even so, such scenarios often arise in practice, such as when sorting integers from a known range or sorting character strings, so discussing them is worthwhile. In this section, we consider the problem of sorting a sequence of entries, each a key-value pair, where the keys have a restricted type.

**Bucket-Sort**  
Consider a sequence _S_ of _n_ entries whose keys are integers in the range \[0,_N_ − 1\], for some integer _N_ ≥ 2, and suppose that _S_ should be sorted according to the keys of the entries. In this case, it is possible to sort _S_ in _O_(_n_ + _N_) time. It might seem surprising, but this implies, for example, that if _N_ is _O_(_n_), then we can sort _S_ in _O_(_n_) time. Of course, the crucial point is that, because of the restrictive assumption about the format of the elements, we can avoid using comparisons.

The main idea is to use an algorithm called _**bucket-sort**_, which is not based on comparisons, but on using keys as indices into a bucket array _B_ that has cells indexed from 0 to _N_ − 1. An entry with key _k_ is placed in the "bucket" _B_\[_k_\], which itself is a sequence (of entries with key _k_). After inserting each entry of the input sequence _S_ into its bucket, we can put the entries back into _S_ in sorted order by enumerating the contents of the buckets _B_\[0\],_B_\[1\], . . . ,_B_\[_N_ − 1\] in order. We describe the bucket-sort algorithm in Code Fragment 12.7.

```
**Algorithm** *bucketSort(S)*:

def bucket_sort(S, N):
    """Sort sequence S of entries with integer keys in range [0, N-1]."""
    B = [[] for _ in range(N)]
    for e in S:
        k = e[0]
        B[k].append(e)
    S.clear()
    for i in range(N):
        S.extend(B[i])

# Example usage
S = [(3, 'a'), (1, 'b'), (2, 'c'), (1, 'd'), (2, 'e'), (1, 'f'), (3, 'g'), (2, 'h')]
N = 4
bucket_sort(S, N)
print(S)
```

**Code Fragment 12.7: Bucket-sort.**

It is easy to see that bucket-sort runs in _O_(_n_ + _N_) time and uses _O_(_n_ + _N_) space. Hence, bucket-sort is efficient when the range _N_ of values for the keys is small compared to the sequence size _n_, say _N_ = _O_(_n_) or _N_ = _O_(_n_ log _n_). Still, its performance deteriorates as _N_ grows compared to _n_.

An important property of the bucket-sort algorithm is that it works correctly even if there are many different elements with the same key. Indeed, we described it in a way that anticipates such occurrences.

**Stable Sorting**  
When sorting key-value pairs, an important issue is how equal keys are handled. Let _S_ = ((_k_<sub>0</sub>,_v_<sub>0</sub>), . . . ,(_k<sub>n</sub>_<sub>−1</sub>,_v<sub>n</sub>_<sub>−1</sub>)) be a sequence of such entries. We say that a sorting algorithm is _**stable**_ if, for any two entries (_k<sub>i</sub>_,_v<sub>i</sub>_) and (_k<sub>j</sub>_,_v<sub>j</sub>_) of _S_ such that _k<sub>i</sub>_ = _k<sub>j</sub>_ and (_k<sub>i</sub>_,_v<sub>i</sub>_) precedes (_k<sub>j</sub>_,_v<sub>j</sub>_) in _S_ before sorting (that is, _i_ < _j_), entry (_k<sub>i</sub>_,_v<sub>i</sub>_) also precedes entry (_k<sub>j</sub>_,_v<sub>j</sub>_) after sorting. Stability is important for a sorting algorithm because applications may want to preserve the initial order of elements with the same key.

Our informal description of bucket-sort in Code Fragment 12.7 guarantees stability as long as we ensure that all sequences act as queues, with elements processed and removed from the front of a sequence and inserted at the back. That is, when initially placing elements of _S_ into buckets, we should process _S_ from front to back, and add each element to the end of its bucket. Subsequently, when transferring elements from the buckets back to _S_, we should process each _B_\[_i_\] from front to back, with those elements added to the end of _S_.

**Radix-Sort**  
One of the reasons that stable sorting is so important is that it allows the bucket-sort approach to be applied to more general contexts than to sort integers. Suppose, for example, that we want to sort entries with keys that are pairs (_k_,_l_), where _k_ and _l_ are integers in the range \[0,_N_ − 1\], for some integer _N_ ≥ 2. In a context such as this, it is common to define an order on these keys using the _**lexicographic**_ (dictionary) convention, where (_k_<sub>1</sub>,_l_<sub>1</sub>) < (_k_<sub>2</sub>,_l_<sub>2</sub>) if _k_<sub>1</sub> < _k_<sub>2</sub> or if _k_<sub>1</sub> = _k_<sub>2</sub> and _l_<sub>1</sub> < _l_<sub>2</sub>. This is a pairwise version of the lexicographic comparison function, which can be applied to equal-length character strings, or to tuples of length _d_.

The _**radix-sort**_ algorithm sorts a sequence _S_ of entries with keys that are pairs, by applying a stable bucket-sort on the sequence twice; first using one component of the pair as the key when ordering and then using the second component. But which order is correct? Should we first sort on the _k_'s (the first component) and then on the _l_'s (the second component), or should it be the other way around?

To gain intuition before answering this question, we consider the following example.

**Example 12.5:** _Consider the following sequence _S_ (we show only the keys):_

$S=((3,3), (1,5), (2,5), (1,2), (2,3), (1,7), (3,2), (2,2)).$

_If we sort _S_ stably on the first component, then we get the sequence  
_  
${S}_{1}=((1,5), (1,2), (1,7), (2,5), (2,3), (2,2), (3,3), (3,2)).$

_If we then stably sort this sequence _S_<sub>1</sub> using the second component, we get the sequence  
_  
${S}_{1,2}=((1,2), (2,2), (3,2), (2,3), (3,3), (1,5), (2,5), (1,7))$,

_which is unfortunately not a sorted sequence. On the other hand, if we first stably sort _S_ using the second component, then we get the sequence  
_  
${S}_{2}=((1,2), (3,2), (2,2), (3,3), (2,3), (1,5), (2,5), (1,7)).$

_If we then stably sort sequence _S_<sub>2</sub> using the first component, we get the sequence  
_  
${S}_{2,1}=((1,2), (1,5), (1,7), (2,2), (2,3), (2,5), (3,2), (3,3))$,

_which is indeed sequence _S_ lexicographically ordered.  
_  
So, from this example, we are led to believe that we should first sort using the second component and then again using the first component. This intuition is exactly right. By first stably sorting by the second component and then again by the first component, we guarantee that if two entries are equal in the second sort (by the first component), then their relative order in the starting sequence (which is sorted by the second component) is preserved. Thus, the resulting sequence is guaranteed to be sorted lexicographically every time. We leave to a simple exercise (R-12.18) the determination of how this approach can be extended to triples and other _d_\-tuples of numbers. We can summarize this section as follows:

**Proposition 12.6:** Let _S_ be a sequence of _n_ key-value pairs, each of which has a key (_k_<sub>1</sub>,_k_<sub>2</sub>, . . . ,_k<sub>d</sub>_), where _k<sub>i</sub>_ is an integer in the range \[0,_N_ − 1\] for some integer _N_ ≥ 2. We can sort _S_ lexicographically in time _O_(_d_(_n_ + _N_)) using radix-sort.

Radix sort can be applied to any key that can be viewed as a composite of smaller pieces that are to be sorted lexicographically. For example, we can apply it to sort character strings of moderate length, as each individual character can be represented as an integer value. (Some care is needed to properly handle strings with varying lengths.)
