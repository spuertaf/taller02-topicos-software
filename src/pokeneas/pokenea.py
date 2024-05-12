class Pokenea:
    def __init__(
        self,
        id: int,
        name: str,
        height: str,
        ability: str,
        image: str,
        philosophical_frase: str
    ) -> 'Pokenea':
        self._id = id
        self._name = name
        self._height = height
        self._ability = ability
        self._image = image
        self._philosophical_frase = philosophical_frase
        
    def json(self) -> dict:
        return {
            "id": self._id,
            "name":self._name,
            "height":self._height,
            "ability":self._ability,
            "image": self._image,
            "philosophical_frase": self._philosophical_frase
        }