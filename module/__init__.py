"""

Modules will interface between the WebApp and the collected metrics.
collected metrics will be gathered with scripts in lib/* folders.

These majority of these scripts where pulled from the iovisor/bcc examples
folder.  Additional lib scripts can obviously be added at will.

Methods for storing Metrics:
    1) Databse - useful for environments gathering a large number of metrics
    whether that's from many nodes, or a lower number of nodes, but low intervals

    2) Indexer - This is useful for visualization, but is difficult as the first source
    of storage.  Ideally, the indexer, if used, would receive data from a second source;
    either a non-persistent/persistent queue, Database, or streaming service.

    3) Non-persistent/persistent queue/Streaming service - Useful for if storing data is
    not desired.  If the volume of metrics being reported is capable of being managed well
    without persistance, this is an ideal option.
"""

