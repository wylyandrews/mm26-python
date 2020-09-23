# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import board_pb2 as board__pb2
import character_pb2 as character__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='game',
  syntax='proto3',
  serialized_options=b'\n\036mech.mania.engine.domain.modelB\017GameStateProtos\252\002\016MM26.IO.Models',
  serialized_pb=b'\n\ngame.proto\x12\x04game\x1a\x0b\x62oard.proto\x1a\x0f\x63haracter.proto\"\x96\x03\n\tGameState\x12\x10\n\x08state_id\x18\x01 \x01(\x03\x12\x34\n\x0b\x62oard_names\x18\x02 \x03(\x0b\x32\x1f.game.GameState.BoardNamesEntry\x12\x36\n\x0cplayer_names\x18\x03 \x03(\x0b\x32 .game.GameState.PlayerNamesEntry\x12\x38\n\rmonster_names\x18\x04 \x03(\x0b\x32!.game.GameState.MonsterNamesEntry\x1a?\n\x0f\x42oardNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1b\n\x05value\x18\x02 \x01(\x0b\x32\x0c.board.Board:\x02\x38\x01\x1a\x45\n\x10PlayerNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.character.Player:\x02\x38\x01\x1aG\n\x11MonsterNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.character.Monster:\x02\x38\x01\x42\x42\n\x1emech.mania.engine.domain.modelB\x0fGameStateProtos\xaa\x02\x0eMM26.IO.Modelsb\x06proto3'
  ,
  dependencies=[board__pb2.DESCRIPTOR,character__pb2.DESCRIPTOR,])




_GAMESTATE_BOARDNAMESENTRY = _descriptor.Descriptor(
  name='BoardNamesEntry',
  full_name='game.GameState.BoardNamesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='game.GameState.BoardNamesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='game.GameState.BoardNamesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=313,
)

_GAMESTATE_PLAYERNAMESENTRY = _descriptor.Descriptor(
  name='PlayerNamesEntry',
  full_name='game.GameState.PlayerNamesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='game.GameState.PlayerNamesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='game.GameState.PlayerNamesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=384,
)

_GAMESTATE_MONSTERNAMESENTRY = _descriptor.Descriptor(
  name='MonsterNamesEntry',
  full_name='game.GameState.MonsterNamesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='game.GameState.MonsterNamesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='game.GameState.MonsterNamesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=386,
  serialized_end=457,
)

_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='game.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_id', full_name='game.GameState.state_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='board_names', full_name='game.GameState.board_names', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_names', full_name='game.GameState.player_names', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monster_names', full_name='game.GameState.monster_names', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GAMESTATE_BOARDNAMESENTRY, _GAMESTATE_PLAYERNAMESENTRY, _GAMESTATE_MONSTERNAMESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=457,
)

_GAMESTATE_BOARDNAMESENTRY.fields_by_name['value'].message_type = board__pb2._BOARD
_GAMESTATE_BOARDNAMESENTRY.containing_type = _GAMESTATE
_GAMESTATE_PLAYERNAMESENTRY.fields_by_name['value'].message_type = character__pb2._PLAYER
_GAMESTATE_PLAYERNAMESENTRY.containing_type = _GAMESTATE
_GAMESTATE_MONSTERNAMESENTRY.fields_by_name['value'].message_type = character__pb2._MONSTER
_GAMESTATE_MONSTERNAMESENTRY.containing_type = _GAMESTATE
_GAMESTATE.fields_by_name['board_names'].message_type = _GAMESTATE_BOARDNAMESENTRY
_GAMESTATE.fields_by_name['player_names'].message_type = _GAMESTATE_PLAYERNAMESENTRY
_GAMESTATE.fields_by_name['monster_names'].message_type = _GAMESTATE_MONSTERNAMESENTRY
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {

  'BoardNamesEntry' : _reflection.GeneratedProtocolMessageType('BoardNamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GAMESTATE_BOARDNAMESENTRY,
    '__module__' : 'game_pb2'
    # @@protoc_insertion_point(class_scope:game.GameState.BoardNamesEntry)
    })
  ,

  'PlayerNamesEntry' : _reflection.GeneratedProtocolMessageType('PlayerNamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GAMESTATE_PLAYERNAMESENTRY,
    '__module__' : 'game_pb2'
    # @@protoc_insertion_point(class_scope:game.GameState.PlayerNamesEntry)
    })
  ,

  'MonsterNamesEntry' : _reflection.GeneratedProtocolMessageType('MonsterNamesEntry', (_message.Message,), {
    'DESCRIPTOR' : _GAMESTATE_MONSTERNAMESENTRY,
    '__module__' : 'game_pb2'
    # @@protoc_insertion_point(class_scope:game.GameState.MonsterNamesEntry)
    })
  ,
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:game.GameState)
  })
_sym_db.RegisterMessage(GameState)
_sym_db.RegisterMessage(GameState.BoardNamesEntry)
_sym_db.RegisterMessage(GameState.PlayerNamesEntry)
_sym_db.RegisterMessage(GameState.MonsterNamesEntry)


DESCRIPTOR._options = None
_GAMESTATE_BOARDNAMESENTRY._options = None
_GAMESTATE_PLAYERNAMESENTRY._options = None
_GAMESTATE_MONSTERNAMESENTRY._options = None
# @@protoc_insertion_point(module_scope)
