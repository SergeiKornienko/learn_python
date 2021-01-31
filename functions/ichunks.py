def ichunks(length, source):
    return map(list, zip(*([iter(source)] * length)))
