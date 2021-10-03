from ursina import *

from ursina.mesh_importer import *

app = Ursina()
models = load_model('ferrari-f1-race-car.obj')
modelEntity = Entity(model=models)


app.run()


radial-gradient(var(--gradientColorThree) 23%,var(--gradientColorThreeTransparent) 67% 100%) 385px -24px,radial-gradient(var(--gradientColorOne) 0,var(--gradientColorOneTransparent) 60% 100%) -940px 290px,radial-gradient(var(--gradientColorTwo) 10%,var(--gradientColorTwoTransparent) 60% 100%) -120px 250px,radial-gradient(var(--gradientColorOne) 40%,var(--gradientColorOneTransparent) 57% 100%) 495px -44px,radial-gradient(var(--gradientColorZero) 30%,var(--gradientColorZeroTransparent) 67% 100%) 122px -120px,radial-gradient(var(--gradientColorZero) 10%,var(--gradientColorZeroTransparent) 60% 100%) -420px 120px,radial-gradient(var(--gradientColorTwo) 15%,var(--gradientColorTwoTransparent) 50% 100%) -620px 0,radial-gradient(var(--gradientColorTwo) 25%,var(--gradientColorTwoTransparent) 50% 100%) 520px -250px,var(--gradientColorZero)


    --gradientColorZero: #a960ee;
    --gradientColorOne: #ff333d;
    --gradientColorTwo: #90e0ff;
    --gradientColorThree: #ffcb57;
    --gradientColorZeroTransparent: rgba(169,96,238,0);
    --gradientColorOneTransparent: rgba(255,51,61,0);
    --gradientColorTwoTransparent: rgba(144,224,255,0);
    --gradientColorThreeTransparent: rgba(255,203,87,0);
    --gradientAngle: var(--angleStrong);
    --gradientHeight: calc(100% + var(--sectionPaddingTop) + var(--transformOriginX)*var(--sectionAngleSin));
    --offsetX: var(--gutterWidth);