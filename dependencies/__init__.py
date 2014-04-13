

class CircularDependencyException(Exception):
    pass


class DependencyInspector():
    def __init__(self):
        self._deps = {}

    def add_direct(self, member, deps):
        mem_deps = self._deps.get(member, [])
        if not mem_deps:
            mem_deps = deps.split(' ')
        else:
            raise ValueError('Dependencies for {0} already defined'.format(member))
        self._deps[member] = mem_deps

    def dependencies_for(self, member):
        if not self._deps.get(member, []):
            return []

        deps = []
        return self._find_deps(member, deps)

    def _find_deps(self, member, deps):
        mem_deps = self._deps.get(member, [])
        if not mem_deps:
            return deps

        if set(mem_deps).intersection(set(deps)):
            raise CircularDependencyException()

        deps.extend(mem_deps)
        for d in mem_deps:
            self._find_deps(d, deps)

        return deps
