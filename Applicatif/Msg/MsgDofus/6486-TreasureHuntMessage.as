package com.ankamagames.dofus.network.messages.game.context.roleplay.treasureHunt
{
   import com.ankamagames.dofus.network.ProtocolTypeManager;
   import com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntFlag;
   import com.ankamagames.dofus.network.types.game.context.roleplay.treasureHunt.TreasureHuntStep;
   import com.ankamagames.jerakine.network.CustomDataWrapper;
   import com.ankamagames.jerakine.network.ICustomDataInput;
   import com.ankamagames.jerakine.network.ICustomDataOutput;
   import com.ankamagames.jerakine.network.INetworkMessage;
   import com.ankamagames.jerakine.network.NetworkMessage;
   import com.ankamagames.jerakine.network.utils.FuncTree;
   import flash.utils.ByteArray;
   
   [Trusted]
   public class TreasureHuntMessage extends NetworkMessage implements INetworkMessage
   {
      
      public static const protocolId:uint = 6486;
   
      public function deserializeAs_TreasureHuntMessage(input:ICustomDataInput) : void
      {
         this.questType = input.readByte();
         this.startMapId = input.readDouble();
         var _knownStepsListLen:uint = input.readUnsignedShort();
         for(var _i3:uint = 0; _i3 < _knownStepsListLen; _i3++)
         {
            _id3 = input.readUnsignedShort();
            _item3 = ProtocolTypeManager.getInstance(TreasureHuntStep,_id3);
            _item3.deserialize(input);
            this.knownStepsList.push(_item3);
         }
         this.totalStepCount = input.readByte();
         this.checkPointCurrent = input.readVarUhInt();
         this.checkPointTotal = input.readVarUhInt();
         this.availableRetryCount = input.readInt();
         var _flagsLen:uint = input.readUnsignedShort();
         for(var _i8:uint = 0; _i8 < _flagsLen; _i8++)
         {
            _item8 = new TreasureHuntFlag();
            _item8.deserialize(input);
            this.flags.push(_item8);
         }
      }
      
      private function _knownStepsListFunc(input:ICustomDataInput) : void
      {
         var _id:uint = input.readUnsignedShort();
         var _item:TreasureHuntStep = ProtocolTypeManager.getInstance(TreasureHuntStep,_id);
         _item.deserialize(input);
         this.knownStepsList.push(_item);
      }
      
      
   }
}