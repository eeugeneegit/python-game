import pygame

class Settings:
    def __init__(self) -> None:
        self.__window_width = 640
        self.__window_hight = 480
        self.__win_points = 50
        self.__background = 'images/bg.png'
        self.__icon = 'images/game_icon.png'
        self.__start_player_x = 320
        self.__start_player_y = 400
        self.__font = 'fonts/Nunito-Light.ttf'
        self.__background_sound = 'sound/background_sound.mp3'
        self.__game_over_sound = 'sound/game_over_sound.mp3'
        self.__game_win_sound = 'sound/game_win_sound.mp3'
        self.first_lbl_coords = (150,200)
        self.second_lbl_coords = (150, 250)
        self.third_lbl_coords = (150, 400)

    def getWindowWidth(self) -> int:
        return self.__window_width
    
    def getWindowHight(self) -> int:
        return self.__window_hight
    
    def getWinPoints(self) -> int:
        return self.__win_points
    
    def getBackground(self) -> str:
        return self.__background
    
    def getIcon(self) -> str:
        return self.__icon
    
    def getStartPlayerX(self) -> int:
        return self.__start_player_x
    
    def getStartPlayerY(self) -> int:
        return self.__start_player_y
    
    def getFont(self) -> str:
        return self.__font

    def getSound(self) -> str:
        return self.__background_sound
    
    def getGameOverSound(self) -> str:
        return self.__game_over_sound
    
    def getGameWinSound(self) -> str:
        return self.__game_win_sound

    def getFirstLabelCoords(self) -> tuple:
        return self.first_lbl_coords
    
    def getSecondLabelCoords(self) -> tuple:
        return self.second_lbl_coords
    
    def getThirdLabelCoords(self) -> tuple:
        return self.third_lbl_coords
    
