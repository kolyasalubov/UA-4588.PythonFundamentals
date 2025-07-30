def are_you_playing_banjo(name):
    if name[0] == 'r' or name[0] == 'R':
        return '{} plays banjo'.format(name)
    else:
        return '{} does not play banjo'.format(name)