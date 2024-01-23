@namespace
class SpriteKind:
    wall = SpriteKind.create()

def on_up_pressed():
    global direction
    animation.run_image_animation(mySprite, assets.animation("""
        myAnim3
    """), 155, True)
    direction = 1
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    global projectile
    if direction == 0:
        animation.run_image_animation(mySprite, assets.animation("""
            myAnim7
        """), 100, False)
        pause(50)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            1st attack
        """), mySprite, -125, 0)
        pause(150)
        sprites.destroy(projectile)
    if direction == 3:
        animation.run_image_animation(mySprite, assets.animation("""
            myAnim2
        """), 100, False)
        pause(50)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            2nd attack
        """), mySprite, 125, 0)
        pause(150)
        sprites.destroy(projectile)
    if direction == 2:
        animation.run_image_animation(mySprite,
            assets.animation("""
                attack forward0
            """),
            30,
            False)
        pause(100)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            2nd attack1
        """), mySprite, 0, 150)
        pause(150)
        sprites.destroy(projectile)
    if direction == 1:
        animation.run_image_animation(mySprite, assets.animation("""
            myAnim10
        """), 75, False)
        pause(50)
        projectile = sprites.create_projectile_from_sprite(assets.image("""
            2nd attack0
        """), mySprite, 0, -150)
        pause(150)
        sprites.destroy(projectile)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_down_released():
    global direction
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(assets.image("""
        player
    """))
    direction = 2
controller.down.on_event(ControllerButtonEvent.RELEASED, on_down_released)

def on_left_pressed():
    global direction
    animation.run_image_animation(mySprite, assets.animation("""
        myAnim1
    """), 155, True)
    direction = 0
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_released():
    global direction
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(assets.image("""
        player sidewalk stop
    """))
    direction = 3
controller.right.on_event(ControllerButtonEvent.RELEASED, on_right_released)

def on_left_released():
    global direction
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(assets.image("""
        player sidewalk stop2
    """))
    direction = 0
controller.left.on_event(ControllerButtonEvent.RELEASED, on_left_released)

def on_countdown_end():
    global zombie_speed
    zombie_speed += 10
info.on_countdown_end(on_countdown_end)

def on_right_pressed():
    global direction
    animation.run_image_animation(mySprite,
        assets.animation("""
            myAnim8
        """),
        direction,
        True)
    direction = 3
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    pause(1500)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_up_released():
    global direction
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    mySprite.set_image(assets.image("""
        player sidewalk stop0
    """))
    direction = 1
controller.up.on_event(ControllerButtonEvent.RELEASED, on_up_released)

def on_down_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        myAnim
    """), 155, True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2, effects.disintegrate, 200)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

myEnemy: Sprite = None
iswall = False
projectile: Sprite = None
direction = 0
mySprite: Sprite = None
zombie_speed = 15
info.start_countdown(120)
list2 = 1
zombies_num = 0
hits = 0
info.set_score(0)
mySprite = sprites.create(assets.image("""
    player
"""), SpriteKind.player)
value = 9
info.set_life(value)
tiles.set_current_tilemap(tilemap("""
    level
"""))
mySprite.set_bounce_on_wall(True)
scene.camera_follow_sprite(mySprite)
tiles.place_on_random_tile(mySprite, sprites.vehicle.road_horizontal)
scene.set_background_image(assets.image("""
    myImage
"""))
controller.move_sprite(mySprite)
sttkCount = 0

def on_forever():
    if value == 0:
        mySprite.set_scale(0.75, ScaleAnchor.MIDDLE)
        pause(200)
        mySprite.set_scale(0.5, ScaleAnchor.MIDDLE)
        pause(200)
        mySprite.set_scale(0.25, ScaleAnchor.MIDDLE)
        pause(200)
        mySprite.set_scale(0, ScaleAnchor.MIDDLE)
        pause(200)
forever(on_forever)

def on_forever2():
    if mySprite.is_hitting_tile(CollisionDirection.LEFT):
        info.change_life_by(-1)
        mySprite.start_effect(effects.fire, 500)
        pause(2500)
forever(on_forever2)

def on_forever3():
    if mySprite.is_hitting_tile(CollisionDirection.TOP):
        info.change_life_by(-1)
        mySprite.start_effect(effects.fire, 500)
        pause(2500)
forever(on_forever3)

def on_forever4():
    global iswall
    iswall = not (iswall)
    for wallTile in tiles.get_tiles_by_type(assets.tile("""
        transparency16
    """)):
        tiles.set_wall_at(wallTile, iswall)
forever(on_forever4)

def on_forever5():
    if mySprite.is_hitting_tile(CollisionDirection.RIGHT):
        info.change_life_by(-1)
        mySprite.start_effect(effects.fire, 500)
        pause(2500)
forever(on_forever5)

def on_forever6():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        info.change_life_by(-1)
        mySprite.start_effect(effects.fire, 500)
        pause(2500)
forever(on_forever6)

def on_forever7():
    if info.life() < 9:
        pause(10000)
        info.change_life_by(1)
        mySprite.start_effect(effects.hearts, 500)
        pause(100)
forever(on_forever7)

def on_update_interval():
    global myEnemy
    for index in range(3):
        myEnemy = sprites.create(assets.image("""
            enemy
        """), SpriteKind.enemy)
        myEnemy.set_bounce_on_wall(True)
        tiles.place_on_random_tile(myEnemy, sprites.vehicle.road_horizontal)
        myEnemy.follow(mySprite, zombie_speed)
        myEnemy.set_scale(0.3, ScaleAnchor.MIDDLE)
        pause(200)
game.on_update_interval(10000, on_update_interval)
