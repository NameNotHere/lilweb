import tcod as libtcod
import map_objects.game_map
from render import clear_all, render_all
from entity import Entity
from input_handeler import handle_keys

from map_objects.cellular import cellular_auto
from map_objects.game_map import GameMap

def main():
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150)
    }

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white, 1, 2)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow, 1, 2)
    entities = [npc, player]

    libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial revised', False)
    con = libtcod.console_new(screen_width, screen_height)

    game_map = GameMap(map_width, map_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()


    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, game_map, screen_width, screen_height, colors)
        libtcod.console_flush()
        clear_all(con, entities)

        action = handle_keys(key)

        move = action.get('move')
        exit = action.get('exit')
        refresh = action.get('Refresh')
        fullscreen = action.get('fullscreen')

        if move:
            dx, dy = move
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                player.move(dx, dy)
        if refresh:
            game_map.tiles = cellular_auto(game_map.tiles, map_width, map_height, 20)
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())



if __name__ == '__main__':
    main()

#GAME IDEA
#TRADITIONAL ROUGELIKE with a twist
#Dont delve into dungeons but rather move on through towns
#Bullet hell
#party system or one character?
#at least a hundred items ranging from melee to ranged, armours items that give buffs etc