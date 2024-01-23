namespace SpriteKind {
    export const wall = SpriteKind.create()
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`myAnim3`,
    155,
    true
    )
    direction = 1
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (direction == 0) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`myAnim7`,
        100,
        false
        )
        pause(50)
        projectile = sprites.createProjectileFromSprite(assets.image`1st attack`, mySprite, -125, 0)
        pause(150)
        sprites.destroy(projectile)
    }
    if (direction == 3) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`myAnim2`,
        100,
        false
        )
        pause(50)
        projectile = sprites.createProjectileFromSprite(assets.image`2nd attack`, mySprite, 125, 0)
        pause(150)
        sprites.destroy(projectile)
    }
    if (direction == 2) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`attack forward0`,
        30,
        false
        )
        pause(100)
        projectile = sprites.createProjectileFromSprite(assets.image`2nd attack1`, mySprite, 0, 150)
        pause(150)
        sprites.destroy(projectile)
    }
    if (direction == 1) {
        animation.runImageAnimation(
        mySprite,
        assets.animation`myAnim10`,
        75,
        false
        )
        pause(50)
        projectile = sprites.createProjectileFromSprite(assets.image`2nd attack0`, mySprite, 0, -150)
        pause(150)
        sprites.destroy(projectile)
    }
})
controller.down.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setImage(assets.image`player`)
    direction = 2
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`myAnim1`,
    155,
    true
    )
    direction = 0
})
controller.right.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setImage(assets.image`player sidewalk stop`)
    direction = 3
})
controller.left.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setImage(assets.image`player sidewalk stop2`)
    direction = 0
})
info.onCountdownEnd(function () {
    zombie_speed += 10
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`myAnim8`,
    direction,
    true
    )
    direction = 3
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Player, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    pause(1500)
})
controller.up.onEvent(ControllerButtonEvent.Released, function () {
    animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    mySprite.setImage(assets.image`player sidewalk stop0`)
    direction = 1
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`myAnim`,
    155,
    true
    )
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.disintegrate, 200)
    info.changeScoreBy(1)
})
let myEnemy: Sprite = null
let iswall = false
let projectile: Sprite = null
let direction = 0
let mySprite: Sprite = null
let zombie_speed = 15
info.startCountdown(120)
let list = 1
let zombies_num = 0
let hits = 0
info.setScore(0)
mySprite = sprites.create(assets.image`player`, SpriteKind.Player)
let value = 9
info.setLife(value)
tiles.setCurrentTilemap(tilemap`level`)
mySprite.setBounceOnWall(true)
scene.cameraFollowSprite(mySprite)
tiles.placeOnRandomTile(mySprite, sprites.vehicle.roadHorizontal)
scene.setBackgroundImage(assets.image`myImage`)
controller.moveSprite(mySprite)
let sttkCount = 0
forever(function () {
    if (value == 0) {
        mySprite.setScale(0.75, ScaleAnchor.Middle)
        pause(200)
        mySprite.setScale(0.5, ScaleAnchor.Middle)
        pause(200)
        mySprite.setScale(0.25, ScaleAnchor.Middle)
        pause(200)
        mySprite.setScale(0, ScaleAnchor.Middle)
        pause(200)
    }
})
forever(function () {
    if (mySprite.isHittingTile(CollisionDirection.Left)) {
        info.changeLifeBy(-1)
        mySprite.startEffect(effects.fire, 500)
        pause(2500)
    }
})
forever(function () {
    if (mySprite.isHittingTile(CollisionDirection.Top)) {
        info.changeLifeBy(-1)
        mySprite.startEffect(effects.fire, 500)
        pause(2500)
    }
})
forever(function () {
    iswall = !(iswall)
    for (let wallTile of tiles.getTilesByType(assets.tile`transparency16`)) {
        tiles.setWallAt(wallTile, iswall)
    }
})
forever(function () {
    if (mySprite.isHittingTile(CollisionDirection.Right)) {
        info.changeLifeBy(-1)
        mySprite.startEffect(effects.fire, 500)
        pause(2500)
    }
})
forever(function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        info.changeLifeBy(-1)
        mySprite.startEffect(effects.fire, 500)
        pause(2500)
    }
})
forever(function () {
    if (info.life() < 9) {
        pause(10000)
        info.changeLifeBy(1)
        mySprite.startEffect(effects.hearts, 500)
        pause(100)
    }
})
game.onUpdateInterval(10000, function () {
    for (let index = 0; index < 3; index++) {
        myEnemy = sprites.create(assets.image`enemy`, SpriteKind.Enemy)
        myEnemy.setBounceOnWall(true)
        tiles.placeOnRandomTile(myEnemy, sprites.vehicle.roadHorizontal)
        myEnemy.follow(mySprite, zombie_speed)
        myEnemy.setScale(0.3, ScaleAnchor.Middle)
        pause(200)
    }
})
