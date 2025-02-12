**_ Висновок _**:

1. Insertion Sort дуже повільний на великих масивах (O(n²)). Варто використовувати тільки для малих або майже відсортованих даних.
2. Merge Sort досить швидкий і стабільний, але використовує додаткову пам’ять через рекурсію, проте він підходить для великих наборів даних.
3. Timsort найшвидший з них, тому його використовує Python у своїх стандартних функціях, бо він адаптивний і добре працює на великих наборах даних.

Тому

- Для великого масиву даних — Timsort найефективніший.
- Insertion Sort варто використовувати лише для дуже малих або майже відсортованих масивів, в іншому випадку це займе забагато часу.
- Merge Sort можна використовувати, проте врахохувати, що може знадобиться додаткова памʼять.
