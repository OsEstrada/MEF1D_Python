from Enums import *
from abc import abstractmethod


class item():
    _id = 0
    _x = 0.0
    _node1 = 0
    _node2 = 0
    _value = 0

    def __init__(self):
        pass

        def getId(self):
            return self._id

        def getX(self):
            return self._x

        def getNode1(self):
            return self._node1

        def getNode2(self):
            return self._node2

        def getValue(self):
            return self._value

    @abstractmethod
    def setIntFloat(self, n, r):
        pass

    @abstractmethod
    def setIntIntInt(self, n1, n2, n3):
        pass


class node(item):
    def setIntFloat(self, identifier, x_coordinate):
        self._id = identifier
        self._x = x_coordinate

    def setIntIntInt(self, n1, n2, n3):
        pass


class element(item):
    def setIntFloat(self, n, r):
        pass

    def setIntIntInt(self, identifier, firstnode, secondnode):
        self._node1 = firstnode
        self._node2 = secondnode
        self._id = identifier


class condition(item):
    def setIntFloat(self, node_to_apply, prescribed_value):
        self._node1 = node_to_apply
        self._value = prescribed_value

    def setIntIntInt(self, n1, n2, n3):
        pass


class mesh():
    __parameters = []
    __sizes = []
    __node_list = []
    __element_list = []
    __dirichlet_list = []
    __neumman_list = []

    def __init__(self):
        pass

    def setParameters(self, l, k, Q):
        self.__parameters.insert(PARAMETERS['ELEMENT_LENGHT'], l)
        self.__parameters.insert(PARAMETERS['THERMAL_CONDUCTIVITY'], k)
        self.__parameters.insert(PARAMETERS['HEAT_SOURCE'], Q)

    def getParameter(self, i):
        return self.__parameters[i]

    def getSize(self, i):
        return self.__sizes[i]

    def setSizes(self, nnodes, neltos, ndirich, nneu):
        self.__sizes.insert(SIZES['NODES'], nnodes)
        self.__sizes.insert(SIZES['ELEMENTS'], neltos)
        self.__sizes.insert(SIZES['DIRICHLET'], ndirich)
        self.__sizes.insert(SIZES['NEUMANN'], nneu)

    def getNodes(self):
        return self.__node_list

    def getElements(self):
        return self.__element_list

    def getDirichlet(self):
        return self.__dirichlet_list

    def getNeumann(self):
        return self.__neumman_list

    def getNode(self, i):
        return self.__node_list[i]

    def getElement(self, i):
        return self.__element_list[i]

    def getCondition(self, i, type):
        if type == SIZES['DIRICHLET']:
            return self.__dirichlet_list[i]
        else:
            return self.__neumman_list[i]


emp = mesh()
