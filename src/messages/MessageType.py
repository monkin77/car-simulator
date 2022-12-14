from enum import IntEnum


class MessageType(IntEnum):
    AccelleratorPedalPosition = 0x01
    BrakePedalPosition = 0x02
    Engine = 0x03
    BrakeSystem = 0x04
    ParkingBrake = 0x05
    CarStatus = 0x06


# care that can bus can only take bytearrays of max len 8
_messageFormats = {
    MessageType.AccelleratorPedalPosition.value: "B",
    MessageType.BrakePedalPosition.value: "B",
    MessageType.Engine.value: "fH",
    MessageType.BrakeSystem.value: "f",
    MessageType.ParkingBrake.value: "?",
    MessageType.CarStatus.value: "fB",
}
