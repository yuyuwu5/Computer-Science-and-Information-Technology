from mininet.topo import Topo
class MyTopo(Topo):
	def __init__(self):
		Topo.__init__(self)
		H1=self.addHost('h1')
		H2=self.addHost('h2')
		H3=self.addHost('h3')
		H4=self.addHost('h4')
		S1=self.addSwitch('s1')

		self.addLink(H1,S1)
		self.addLink(H2,S1)
		self.addLink(H3,S1)
		self.addLink(H4,S1)

		
topos={'mytopo':(lambda:MyTopo())}
