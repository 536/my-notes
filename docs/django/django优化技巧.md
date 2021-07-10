# django优化技巧

* queryset为大数据集

如果仅使用一次的数据集，可以使用query.iterator()，这样可以避免一次性缓存大量数据，实现降低内存占用的目的

* queryset需要进行分页

paginator使用的query不必包含所有字段，设置query.only('id')可以减少所获取的数据字段数目，从而提高数据库读取效率
