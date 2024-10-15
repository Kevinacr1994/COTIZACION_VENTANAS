class Ventana:
    PRECIOS_ACABADO = {
        'Pulido': 50700,
        'Lacado Brillante': 54200,
        'Lacado Mate': 53600,
        'Anodizado': 57300
    }
    PRECIOS_VIDRIO = {
        'Transparente': 8.25,
        'Bronce': 9.15,
        'Azul': 12.75
    }
    PRECIO_ESMERILADO = 5.20
    PRECIO_CHAPA = 16200
    PRECIO_ESQUINA = 4310
    
  def __init__(self, ancho, alto, estilo, vidrio, esmerilado=False):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.vidrio = vidrio
        self.esmerilado = esmerilado