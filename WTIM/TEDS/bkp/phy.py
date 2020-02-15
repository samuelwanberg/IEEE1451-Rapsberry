from teds import TEDS


class PhyTedsReads(TEDS):
    
    def __init__(self, filename='phyteds.json'):
        
        self.name = "PhyTeds"
        super().__init__(self.name, filename)

        self.blockcode = {
            "Radio": "0A",
            "MaxBPS": "0B", 
            "MaxCDev": "0C", 
            "MaxRDev": "0D", 
            "Ecrypt": "0E",
            "Authent": "0F", 
            "MaxSDU": "12",
            "MinALat": "13", 
            "MinTLat": "14", 
            "MaxXact": "15", 
            "Baterry": "16", 
            "Version": "17", 
            "MaxRetry": "18", 
            "Phy_Ch": "40",
            "Phy_ch_w": "41", 
            "phyFreq": "43", 
            "RangeMax": "44"
        }
