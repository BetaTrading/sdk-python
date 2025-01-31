# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmos/group/v1/tx.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyinjective.proto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from pyinjective.proto.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from pyinjective.proto.cosmos.group.v1 import types_pb2 as cosmos_dot_group_dot_v1_dot_types__pb2
from pyinjective.proto.cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from pyinjective.proto.amino import amino_pb2 as amino_dot_amino__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x18\x63osmos/group/v1/tx.proto\x12\x0f\x63osmos.group.v1\x1a\x14gogoproto/gogo.proto\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x1b\x63osmos/group/v1/types.proto\x1a\x17\x63osmos/msg/v1/msg.proto\x1a\x11\x61mino/amino.proto"\xcb\x01\n\x0eMsgCreateGroup\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x43\n\x07members\x18\x02 \x03(\x0b\x32\x1e.cosmos.group.v1.MemberRequestB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07members\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata:(\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\x19\x63osmos-sdk/MsgCreateGroup"3\n\x16MsgCreateGroupResponse\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId"\xe5\x01\n\x15MsgUpdateGroupMembers\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x19\n\x08group_id\x18\x02 \x01(\x04R\x07groupId\x12P\n\x0emember_updates\x18\x03 \x03(\x0b\x32\x1e.cosmos.group.v1.MemberRequestB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\rmemberUpdates:/\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0* cosmos-sdk/MsgUpdateGroupMembers"\x1f\n\x1dMsgUpdateGroupMembersResponse"\xc6\x01\n\x13MsgUpdateGroupAdmin\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x19\n\x08group_id\x18\x02 \x01(\x04R\x07groupId\x12\x35\n\tnew_admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08newAdmin:-\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\x1e\x63osmos-sdk/MsgUpdateGroupAdmin"\x1d\n\x1bMsgUpdateGroupAdminResponse"\xb1\x01\n\x16MsgUpdateGroupMetadata\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x19\n\x08group_id\x18\x02 \x01(\x04R\x07groupId\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata:0\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*!cosmos-sdk/MsgUpdateGroupMetadata" \n\x1eMsgUpdateGroupMetadataResponse"\x94\x02\n\x14MsgCreateGroupPolicy\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x19\n\x08group_id\x18\x02 \x01(\x04R\x07groupId\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\x12\x61\n\x0f\x64\x65\x63ision_policy\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyB"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicyR\x0e\x64\x65\x63isionPolicy:2\x88\xa0\x1f\x00\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\x1f\x63osmos-sdk/MsgCreateGroupPolicy"R\n\x1cMsgCreateGroupPolicyResponse\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress"\x83\x02\n\x19MsgUpdateGroupPolicyAdmin\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12J\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12groupPolicyAddress\x12\x35\n\tnew_admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08newAdmin:3\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*$cosmos-sdk/MsgUpdateGroupPolicyAdmin"#\n!MsgUpdateGroupPolicyAdminResponse"\xb8\x03\n\x18MsgCreateGroupWithPolicy\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12\x43\n\x07members\x18\x02 \x03(\x0b\x32\x1e.cosmos.group.v1.MemberRequestB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01R\x07members\x12%\n\x0egroup_metadata\x18\x03 \x01(\tR\rgroupMetadata\x12\x32\n\x15group_policy_metadata\x18\x04 \x01(\tR\x13groupPolicyMetadata\x12\x31\n\x15group_policy_as_admin\x18\x05 \x01(\x08R\x12groupPolicyAsAdmin\x12\x61\n\x0f\x64\x65\x63ision_policy\x18\x06 \x01(\x0b\x32\x14.google.protobuf.AnyB"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicyR\x0e\x64\x65\x63isionPolicy:6\x88\xa0\x1f\x00\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*#cosmos-sdk/MsgCreateGroupWithPolicy"\x89\x01\n MsgCreateGroupWithPolicyResponse\x12\x19\n\x08group_id\x18\x01 \x01(\x04R\x07groupId\x12J\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12groupPolicyAddress"\xbf\x02\n"MsgUpdateGroupPolicyDecisionPolicy\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12J\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12groupPolicyAddress\x12\x61\n\x0f\x64\x65\x63ision_policy\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB"\xca\xb4-\x1e\x63osmos.group.v1.DecisionPolicyR\x0e\x64\x65\x63isionPolicy::\x88\xa0\x1f\x00\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\'cosmos-sdk/MsgUpdateGroupDecisionPolicy",\n*MsgUpdateGroupPolicyDecisionPolicyResponse"\xee\x01\n\x1cMsgUpdateGroupPolicyMetadata\x12.\n\x05\x61\x64min\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05\x61\x64min\x12J\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12groupPolicyAddress\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata:6\x82\xe7\xb0*\x05\x61\x64min\x8a\xe7\xb0*\'cosmos-sdk/MsgUpdateGroupPolicyMetadata"&\n$MsgUpdateGroupPolicyMetadataResponse"\xe1\x02\n\x11MsgSubmitProposal\x12J\n\x14group_policy_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x12groupPolicyAddress\x12\x1c\n\tproposers\x18\x02 \x03(\tR\tproposers\x12\x1a\n\x08metadata\x18\x03 \x01(\tR\x08metadata\x12\x30\n\x08messages\x18\x04 \x03(\x0b\x32\x14.google.protobuf.AnyR\x08messages\x12)\n\x04\x65xec\x18\x05 \x01(\x0e\x32\x15.cosmos.group.v1.ExecR\x04\x65xec\x12\x14\n\x05title\x18\x06 \x01(\tR\x05title\x12\x18\n\x07summary\x18\x07 \x01(\tR\x07summary:9\x88\xa0\x1f\x00\x82\xe7\xb0*\tproposers\x8a\xe7\xb0*"cosmos-sdk/group/MsgSubmitProposal"<\n\x19MsgSubmitProposalResponse\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId"\xa1\x01\n\x13MsgWithdrawProposal\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12\x32\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress:5\x82\xe7\xb0*\x07\x61\x64\x64ress\x8a\xe7\xb0*$cosmos-sdk/group/MsgWithdrawProposal"\x1d\n\x1bMsgWithdrawProposalResponse"\xff\x01\n\x07MsgVote\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12.\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x05voter\x12\x33\n\x06option\x18\x03 \x01(\x0e\x32\x1b.cosmos.group.v1.VoteOptionR\x06option\x12\x1a\n\x08metadata\x18\x04 \x01(\tR\x08metadata\x12)\n\x04\x65xec\x18\x05 \x01(\x0e\x32\x15.cosmos.group.v1.ExecR\x04\x65xec:\'\x82\xe7\xb0*\x05voter\x8a\xe7\xb0*\x18\x63osmos-sdk/group/MsgVote"\x11\n\x0fMsgVoteResponse"\x8c\x01\n\x07MsgExec\x12\x1f\n\x0bproposal_id\x18\x01 \x01(\x04R\nproposalId\x12\x34\n\x08\x65xecutor\x18\x02 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x08\x65xecutor:*\x82\xe7\xb0*\x08\x65xecutor\x8a\xe7\xb0*\x18\x63osmos-sdk/group/MsgExec"R\n\x0fMsgExecResponse\x12?\n\x06result\x18\x02 \x01(\x0e\x32\'.cosmos.group.v1.ProposalExecutorResultR\x06result"\x8f\x01\n\rMsgLeaveGroup\x12\x32\n\x07\x61\x64\x64ress\x18\x01 \x01(\tB\x18\xd2\xb4-\x14\x63osmos.AddressStringR\x07\x61\x64\x64ress\x12\x19\n\x08group_id\x18\x02 \x01(\x04R\x07groupId:/\x82\xe7\xb0*\x07\x61\x64\x64ress\x8a\xe7\xb0*\x1e\x63osmos-sdk/group/MsgLeaveGroup"\x17\n\x15MsgLeaveGroupResponse**\n\x04\x45xec\x12\x14\n\x10\x45XEC_UNSPECIFIED\x10\x00\x12\x0c\n\x08\x45XEC_TRY\x10\x01\x32\xca\x0b\n\x03Msg\x12W\n\x0b\x43reateGroup\x12\x1f.cosmos.group.v1.MsgCreateGroup\x1a\'.cosmos.group.v1.MsgCreateGroupResponse\x12l\n\x12UpdateGroupMembers\x12&.cosmos.group.v1.MsgUpdateGroupMembers\x1a..cosmos.group.v1.MsgUpdateGroupMembersResponse\x12\x66\n\x10UpdateGroupAdmin\x12$.cosmos.group.v1.MsgUpdateGroupAdmin\x1a,.cosmos.group.v1.MsgUpdateGroupAdminResponse\x12o\n\x13UpdateGroupMetadata\x12\'.cosmos.group.v1.MsgUpdateGroupMetadata\x1a/.cosmos.group.v1.MsgUpdateGroupMetadataResponse\x12i\n\x11\x43reateGroupPolicy\x12%.cosmos.group.v1.MsgCreateGroupPolicy\x1a-.cosmos.group.v1.MsgCreateGroupPolicyResponse\x12u\n\x15\x43reateGroupWithPolicy\x12).cosmos.group.v1.MsgCreateGroupWithPolicy\x1a\x31.cosmos.group.v1.MsgCreateGroupWithPolicyResponse\x12x\n\x16UpdateGroupPolicyAdmin\x12*.cosmos.group.v1.MsgUpdateGroupPolicyAdmin\x1a\x32.cosmos.group.v1.MsgUpdateGroupPolicyAdminResponse\x12\x93\x01\n\x1fUpdateGroupPolicyDecisionPolicy\x12\x33.cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicy\x1a;.cosmos.group.v1.MsgUpdateGroupPolicyDecisionPolicyResponse\x12\x81\x01\n\x19UpdateGroupPolicyMetadata\x12-.cosmos.group.v1.MsgUpdateGroupPolicyMetadata\x1a\x35.cosmos.group.v1.MsgUpdateGroupPolicyMetadataResponse\x12`\n\x0eSubmitProposal\x12".cosmos.group.v1.MsgSubmitProposal\x1a*.cosmos.group.v1.MsgSubmitProposalResponse\x12\x66\n\x10WithdrawProposal\x12$.cosmos.group.v1.MsgWithdrawProposal\x1a,.cosmos.group.v1.MsgWithdrawProposalResponse\x12\x42\n\x04Vote\x12\x18.cosmos.group.v1.MsgVote\x1a .cosmos.group.v1.MsgVoteResponse\x12\x42\n\x04\x45xec\x12\x18.cosmos.group.v1.MsgExec\x1a .cosmos.group.v1.MsgExecResponse\x12T\n\nLeaveGroup\x12\x1e.cosmos.group.v1.MsgLeaveGroup\x1a&.cosmos.group.v1.MsgLeaveGroupResponse\x1a\x05\x80\xe7\xb0*\x01\x42\xa2\x01\n\x13\x63om.cosmos.group.v1B\x07TxProtoP\x01Z$github.com/cosmos/cosmos-sdk/x/group\xa2\x02\x03\x43GX\xaa\x02\x0f\x43osmos.Group.V1\xca\x02\x0f\x43osmos\\Group\\V1\xe2\x02\x1b\x43osmos\\Group\\V1\\GPBMetadata\xea\x02\x11\x43osmos::Group::V1b\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "cosmos.group.v1.tx_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals["DESCRIPTOR"]._loaded_options = None
    _globals["DESCRIPTOR"]._serialized_options = (
        b"\n\023com.cosmos.group.v1B\007TxProtoP\001Z$github.com/cosmos/cosmos-sdk/x/group\242\002\003CGX\252\002\017Cosmos.Group.V1\312\002\017Cosmos\\Group\\V1\342\002\033Cosmos\\Group\\V1\\GPBMetadata\352\002\021Cosmos::Group::V1"
    )
    _globals["_MSGCREATEGROUP"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGCREATEGROUP"].fields_by_name["admin"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGCREATEGROUP"].fields_by_name["members"]._loaded_options = None
    _globals["_MSGCREATEGROUP"].fields_by_name["members"]._serialized_options = b"\310\336\037\000\250\347\260*\001"
    _globals["_MSGCREATEGROUP"]._loaded_options = None
    _globals["_MSGCREATEGROUP"]._serialized_options = (
        b"\202\347\260*\005admin\212\347\260*\031cosmos-sdk/MsgCreateGroup"
    )
    _globals["_MSGUPDATEGROUPMEMBERS"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPMEMBERS"].fields_by_name[
        "admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPMEMBERS"].fields_by_name["member_updates"]._loaded_options = None
    _globals["_MSGUPDATEGROUPMEMBERS"].fields_by_name[
        "member_updates"
    ]._serialized_options = b"\310\336\037\000\250\347\260*\001"
    _globals["_MSGUPDATEGROUPMEMBERS"]._loaded_options = None
    _globals["_MSGUPDATEGROUPMEMBERS"]._serialized_options = (
        b"\202\347\260*\005admin\212\347\260* cosmos-sdk/MsgUpdateGroupMembers"
    )
    _globals["_MSGUPDATEGROUPADMIN"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPADMIN"].fields_by_name["admin"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPADMIN"].fields_by_name["new_admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPADMIN"].fields_by_name[
        "new_admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPADMIN"]._loaded_options = None
    _globals["_MSGUPDATEGROUPADMIN"]._serialized_options = (
        b"\202\347\260*\005admin\212\347\260*\036cosmos-sdk/MsgUpdateGroupAdmin"
    )
    _globals["_MSGUPDATEGROUPMETADATA"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPMETADATA"].fields_by_name[
        "admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPMETADATA"]._loaded_options = None
    _globals["_MSGUPDATEGROUPMETADATA"]._serialized_options = (
        b"\202\347\260*\005admin\212\347\260*!cosmos-sdk/MsgUpdateGroupMetadata"
    )
    _globals["_MSGCREATEGROUPPOLICY"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGCREATEGROUPPOLICY"].fields_by_name["admin"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGCREATEGROUPPOLICY"].fields_by_name["decision_policy"]._loaded_options = None
    _globals["_MSGCREATEGROUPPOLICY"].fields_by_name[
        "decision_policy"
    ]._serialized_options = b"\312\264-\036cosmos.group.v1.DecisionPolicy"
    _globals["_MSGCREATEGROUPPOLICY"]._loaded_options = None
    _globals["_MSGCREATEGROUPPOLICY"]._serialized_options = (
        b"\210\240\037\000\202\347\260*\005admin\212\347\260*\037cosmos-sdk/MsgCreateGroupPolicy"
    )
    _globals["_MSGCREATEGROUPPOLICYRESPONSE"].fields_by_name["address"]._loaded_options = None
    _globals["_MSGCREATEGROUPPOLICYRESPONSE"].fields_by_name[
        "address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYADMIN"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYADMIN"].fields_by_name[
        "admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYADMIN"].fields_by_name["group_policy_address"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYADMIN"].fields_by_name[
        "group_policy_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYADMIN"].fields_by_name["new_admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYADMIN"].fields_by_name[
        "new_admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYADMIN"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYADMIN"]._serialized_options = (
        b"\202\347\260*\005admin\212\347\260*$cosmos-sdk/MsgUpdateGroupPolicyAdmin"
    )
    _globals["_MSGCREATEGROUPWITHPOLICY"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGCREATEGROUPWITHPOLICY"].fields_by_name[
        "admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGCREATEGROUPWITHPOLICY"].fields_by_name["members"]._loaded_options = None
    _globals["_MSGCREATEGROUPWITHPOLICY"].fields_by_name[
        "members"
    ]._serialized_options = b"\310\336\037\000\250\347\260*\001"
    _globals["_MSGCREATEGROUPWITHPOLICY"].fields_by_name["decision_policy"]._loaded_options = None
    _globals["_MSGCREATEGROUPWITHPOLICY"].fields_by_name[
        "decision_policy"
    ]._serialized_options = b"\312\264-\036cosmos.group.v1.DecisionPolicy"
    _globals["_MSGCREATEGROUPWITHPOLICY"]._loaded_options = None
    _globals["_MSGCREATEGROUPWITHPOLICY"]._serialized_options = (
        b"\210\240\037\000\202\347\260*\005admin\212\347\260*#cosmos-sdk/MsgCreateGroupWithPolicy"
    )
    _globals["_MSGCREATEGROUPWITHPOLICYRESPONSE"].fields_by_name["group_policy_address"]._loaded_options = None
    _globals["_MSGCREATEGROUPWITHPOLICYRESPONSE"].fields_by_name[
        "group_policy_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"].fields_by_name[
        "admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"].fields_by_name["group_policy_address"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"].fields_by_name[
        "group_policy_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"].fields_by_name["decision_policy"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"].fields_by_name[
        "decision_policy"
    ]._serialized_options = b"\312\264-\036cosmos.group.v1.DecisionPolicy"
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"]._serialized_options = (
        b"\210\240\037\000\202\347\260*\005admin\212\347\260*'cosmos-sdk/MsgUpdateGroupDecisionPolicy"
    )
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"].fields_by_name["admin"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"].fields_by_name[
        "admin"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"].fields_by_name["group_policy_address"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"].fields_by_name[
        "group_policy_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"]._loaded_options = None
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"]._serialized_options = (
        b"\202\347\260*\005admin\212\347\260*'cosmos-sdk/MsgUpdateGroupPolicyMetadata"
    )
    _globals["_MSGSUBMITPROPOSAL"].fields_by_name["group_policy_address"]._loaded_options = None
    _globals["_MSGSUBMITPROPOSAL"].fields_by_name[
        "group_policy_address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGSUBMITPROPOSAL"]._loaded_options = None
    _globals["_MSGSUBMITPROPOSAL"]._serialized_options = (
        b'\210\240\037\000\202\347\260*\tproposers\212\347\260*"cosmos-sdk/group/MsgSubmitProposal'
    )
    _globals["_MSGWITHDRAWPROPOSAL"].fields_by_name["address"]._loaded_options = None
    _globals["_MSGWITHDRAWPROPOSAL"].fields_by_name[
        "address"
    ]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGWITHDRAWPROPOSAL"]._loaded_options = None
    _globals["_MSGWITHDRAWPROPOSAL"]._serialized_options = (
        b"\202\347\260*\007address\212\347\260*$cosmos-sdk/group/MsgWithdrawProposal"
    )
    _globals["_MSGVOTE"].fields_by_name["voter"]._loaded_options = None
    _globals["_MSGVOTE"].fields_by_name["voter"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGVOTE"]._loaded_options = None
    _globals["_MSGVOTE"]._serialized_options = b"\202\347\260*\005voter\212\347\260*\030cosmos-sdk/group/MsgVote"
    _globals["_MSGEXEC"].fields_by_name["executor"]._loaded_options = None
    _globals["_MSGEXEC"].fields_by_name["executor"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGEXEC"]._loaded_options = None
    _globals["_MSGEXEC"]._serialized_options = b"\202\347\260*\010executor\212\347\260*\030cosmos-sdk/group/MsgExec"
    _globals["_MSGLEAVEGROUP"].fields_by_name["address"]._loaded_options = None
    _globals["_MSGLEAVEGROUP"].fields_by_name["address"]._serialized_options = b"\322\264-\024cosmos.AddressString"
    _globals["_MSGLEAVEGROUP"]._loaded_options = None
    _globals["_MSGLEAVEGROUP"]._serialized_options = (
        b"\202\347\260*\007address\212\347\260*\036cosmos-sdk/group/MsgLeaveGroup"
    )
    _globals["_MSG"]._loaded_options = None
    _globals["_MSG"]._serialized_options = b"\200\347\260*\001"
    _globals["_EXEC"]._serialized_start = 4346
    _globals["_EXEC"]._serialized_end = 4388
    _globals["_MSGCREATEGROUP"]._serialized_start = 195
    _globals["_MSGCREATEGROUP"]._serialized_end = 398
    _globals["_MSGCREATEGROUPRESPONSE"]._serialized_start = 400
    _globals["_MSGCREATEGROUPRESPONSE"]._serialized_end = 451
    _globals["_MSGUPDATEGROUPMEMBERS"]._serialized_start = 454
    _globals["_MSGUPDATEGROUPMEMBERS"]._serialized_end = 683
    _globals["_MSGUPDATEGROUPMEMBERSRESPONSE"]._serialized_start = 685
    _globals["_MSGUPDATEGROUPMEMBERSRESPONSE"]._serialized_end = 716
    _globals["_MSGUPDATEGROUPADMIN"]._serialized_start = 719
    _globals["_MSGUPDATEGROUPADMIN"]._serialized_end = 917
    _globals["_MSGUPDATEGROUPADMINRESPONSE"]._serialized_start = 919
    _globals["_MSGUPDATEGROUPADMINRESPONSE"]._serialized_end = 948
    _globals["_MSGUPDATEGROUPMETADATA"]._serialized_start = 951
    _globals["_MSGUPDATEGROUPMETADATA"]._serialized_end = 1128
    _globals["_MSGUPDATEGROUPMETADATARESPONSE"]._serialized_start = 1130
    _globals["_MSGUPDATEGROUPMETADATARESPONSE"]._serialized_end = 1162
    _globals["_MSGCREATEGROUPPOLICY"]._serialized_start = 1165
    _globals["_MSGCREATEGROUPPOLICY"]._serialized_end = 1441
    _globals["_MSGCREATEGROUPPOLICYRESPONSE"]._serialized_start = 1443
    _globals["_MSGCREATEGROUPPOLICYRESPONSE"]._serialized_end = 1525
    _globals["_MSGUPDATEGROUPPOLICYADMIN"]._serialized_start = 1528
    _globals["_MSGUPDATEGROUPPOLICYADMIN"]._serialized_end = 1787
    _globals["_MSGUPDATEGROUPPOLICYADMINRESPONSE"]._serialized_start = 1789
    _globals["_MSGUPDATEGROUPPOLICYADMINRESPONSE"]._serialized_end = 1824
    _globals["_MSGCREATEGROUPWITHPOLICY"]._serialized_start = 1827
    _globals["_MSGCREATEGROUPWITHPOLICY"]._serialized_end = 2267
    _globals["_MSGCREATEGROUPWITHPOLICYRESPONSE"]._serialized_start = 2270
    _globals["_MSGCREATEGROUPWITHPOLICYRESPONSE"]._serialized_end = 2407
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"]._serialized_start = 2410
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICY"]._serialized_end = 2729
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE"]._serialized_start = 2731
    _globals["_MSGUPDATEGROUPPOLICYDECISIONPOLICYRESPONSE"]._serialized_end = 2775
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"]._serialized_start = 2778
    _globals["_MSGUPDATEGROUPPOLICYMETADATA"]._serialized_end = 3016
    _globals["_MSGUPDATEGROUPPOLICYMETADATARESPONSE"]._serialized_start = 3018
    _globals["_MSGUPDATEGROUPPOLICYMETADATARESPONSE"]._serialized_end = 3056
    _globals["_MSGSUBMITPROPOSAL"]._serialized_start = 3059
    _globals["_MSGSUBMITPROPOSAL"]._serialized_end = 3412
    _globals["_MSGSUBMITPROPOSALRESPONSE"]._serialized_start = 3414
    _globals["_MSGSUBMITPROPOSALRESPONSE"]._serialized_end = 3474
    _globals["_MSGWITHDRAWPROPOSAL"]._serialized_start = 3477
    _globals["_MSGWITHDRAWPROPOSAL"]._serialized_end = 3638
    _globals["_MSGWITHDRAWPROPOSALRESPONSE"]._serialized_start = 3640
    _globals["_MSGWITHDRAWPROPOSALRESPONSE"]._serialized_end = 3669
    _globals["_MSGVOTE"]._serialized_start = 3672
    _globals["_MSGVOTE"]._serialized_end = 3927
    _globals["_MSGVOTERESPONSE"]._serialized_start = 3929
    _globals["_MSGVOTERESPONSE"]._serialized_end = 3946
    _globals["_MSGEXEC"]._serialized_start = 3949
    _globals["_MSGEXEC"]._serialized_end = 4089
    _globals["_MSGEXECRESPONSE"]._serialized_start = 4091
    _globals["_MSGEXECRESPONSE"]._serialized_end = 4173
    _globals["_MSGLEAVEGROUP"]._serialized_start = 4176
    _globals["_MSGLEAVEGROUP"]._serialized_end = 4319
    _globals["_MSGLEAVEGROUPRESPONSE"]._serialized_start = 4321
    _globals["_MSGLEAVEGROUPRESPONSE"]._serialized_end = 4344
    _globals["_MSG"]._serialized_start = 4391
    _globals["_MSG"]._serialized_end = 5873
# @@protoc_insertion_point(module_scope)
