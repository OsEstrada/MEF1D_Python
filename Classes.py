from Dictionaries import *

#Clase padre la cual posee atributos y funciones que se repetiran en la mayoria de las clases que se utilizaran
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

#Clase que representa a un nodo de una malla
class node(item):
    #Funcion que almacena el id y la coordenada x (unicamente almacena una coordenada por ser 1D)
    def setIntFloat(self, identifier, x_coordinate):
        self._id = identifier
        self._x = x_coordinate

#Clase que representa a un elemento de una malla
class element(item):
    #Funcion que almacena los valores de los nodos, y el identificador del elemento.
    def setIntIntInt(self, identifier, firstnode, secondnode):
        self._node1 = firstnode
        self._node2 = secondnode
        self._id = identifier

#Clase que representa a las condiciones de contorno
class condition(item):
    #Funcion que almacena el nodo en que se aplica la condicion(Neumann o Dirichlet) y el identificador del elemento
    def setIntFloat(self, node_to_apply, prescribed_value):
        self._node1 = node_to_apply
        self._value = prescribed_value

#Clase que representa la malla con la cual se discretizara la ecuacion de Poisson
class mesh():
    #Atributos que representan las listas de elementos que se utilizaran durante el calculo
    __parameters = []
    __sizes = []
    __node_list = []
    __element_list = []
    __dirichlet_list = []
    __neumman_list = []

    def __init__(self):
        pass

    #Se alamcena en la lista de parametros los valores de l, k y Q
    def setParameters(self, l, k, Q):
        self.__parameters.insert(PARAMETERS['ELEMENT_LENGHT'], l)
        self.__parameters.insert(PARAMETERS['THERMAL_CONDUCTIVITY'], k)
        self.__parameters.insert(PARAMETERS['HEAT_SOURCE'], Q)

    #Se almacenan los datos  correspondientes al numero de nodos, elementos de la malla, condiciones de dirichlet
    # y condiciones de neumann
    def setSizes(self, nnodes, neltos, ndirich, nneu):
        self.__sizes.insert(SIZES['NODES'], nnodes)
        self.__sizes.insert(SIZES['ELEMENTS'], neltos)
        self.__sizes.insert(SIZES['DIRICHLET'], ndirich)
        self.__sizes.insert(SIZES['NEUMANN'], nneu)

    #Se instancian las listas a utilizar en el objeto mesh, y se instancian a su vez los objetos que estos almacenaran.
    def createData(self):
        for i in range(self.__sizes[SIZES['NODES']]):
            self.__node_list.append(node())
        for i in range(self.__sizes[SIZES['ELEMENTS']]):
            self.__element_list.append(element())
        for i in range(self.__sizes[SIZES['DIRICHLET']]):
            self.__dirichlet_list.append(condition())
        for i in range(self.__sizes[SIZES['NEUMANN']]):
            self.__neumman_list.append(condition())

    #Getters de cada uno de los atributos que posee la clase mesh

    def getParameter(self, i):
        return self.__parameters[i]

    def getSize(self, i):
        return self.__sizes[i]

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
        #Se verifica en base al paremtro type, cual es el tipo de condicion a utilizar, si es dirichlet o si es neumann
        if type == SIZES['DIRICHLET']:
            return self.__dirichlet_list[i]
        else:
            return self.__neumman_list[i]