import sys
import os
import zipfile

save_name = sys.argv[1]
save_file = "{}/AppData/LocalLow/Owlcat Games/Pathfinder Kingmaker/Saved Games/{}".format(os.environ['USERPROFILE'],save_name)
save_zip = zipfile.ZipFile(save_file)

removable = [
"history",
#Boggard Hunting Grounds
"17cfd3e2fa9558c41af6f98274ac2e44.fog.png",
"17cfd3e2fa9558c41af6f98274ac2e44.json",
"17cfd3e2fa9558c41af6f98274ac2e44tuskgutterslair_magicfogmechanics.json",
#Ancient Tomb/Pine Patch
"016ac1a902ff0ce4b905cc65ee01cecd.fog.png",
"016ac1a902ff0ce4b905cc65ee01cecd.json",
"016ac1a902ff0ce4b905cc65ee01cecdradishpatch_magicfogmechanics.json",
"81b13ce8765469045864ffb878b0944b.fog.png",
"81b13ce8765469045864ffb878b0944b.json",
"81b13ce8765469045864ffb878b0944boldcyclopstomb_mechanics02.json",
#Endless Plains
"314e8c3b15b896a4f847c85f9250f02b.fog.png",
"314e8c3b15b896a4f847c85f9250f02b.json",
#Fangberry Cave
"b10e86516b6437d45a629931c30936fe.fog.png",
"b10e86516b6437d45a629931c30936fe.json",
"b10e86516b6437d45a629931c30936fespidercave_magicfogmechanics.json",
"b10e86516b6437d45a629931c30936fespidercaveindoor_mechanics.json",
#Abandoned Hut
"17488ae7967d5894b913e9cfa4e71615.fog.png",
"17488ae7967d5894b913e9cfa4e71615.json",
"17488ae7967d5894b913e9cfa4e71615staglordoldcamp_magicfogmechanics.json",
#Old Sycamore Caves/Depths
"ed22f08d587c8e04a91f48b86e1cc787.fog.png",
"ed22f08d587c8e04a91f48b86e1cc787.json",
"fb4cffc2c4279e141a1c877785bce7ac.fog.png",
"fb4cffc2c4279e141a1c877785bce7ac.json",
#Riverine Rise
"f39f8b5e85775e04c80c566c2c65126f.fog.png",
"f39f8b5e85775e04c80c566c2c65126f.json",
"f39f8b5e85775e04c80c566c2c65126fnorthnarlmarchesregionlair01_magicfogmechanics.json",
#Nettle's Crossing
"4ae70211cd73c1d4884b3b3ff2a61fbb.fog.png",
"4ae70211cd73c1d4884b3b3ff2a61fbb.json",
"4ae70211cd73c1d4884b3b3ff2a61fbbnettlescrossing_magicfogmechanics.json",
#Twin-Rivers Field
"d7477d499b23d48438ef717baa5f1efe.fog.png",
"d7477d499b23d48438ef717baa5f1efe.json",
"d7477d499b23d48438ef717baa5f1efehe2_cr_rangerscamp_magicfogmechanics.json",
#Oak-That-Strayed
"bef8cdb4a53c73848ade605fe516850e.fog.png",
"bef8cdb4a53c73848ade605fe516850e.json",
"bef8cdb4a53c73848ade605fe516850edryadlair_magicfogmechanics.json",
#Old Oak
"a7a165df38562224ebf65e3f10029f15.fog.png",
"a7a165df38562224ebf65e3f10029f15.json",
"a7a165df38562224ebf65e3f10029f15tradingpostregionlair01_magicfogmechanics.json",
#Old Mesa
"dc892947b1d180b44bb202559ecaec33.fog.png",
"dc892947b1d180b44bb202559ecaec33.json",
"dc892947b1d180b44bb202559ecaec33capitalregionlair01_magicfogmechanics.json",
#Glade In The Wilderness
"cffae78b60b80cd458160b4237ecabad.fog.png",
"cffae78b60b80cd458160b4237ecabad.json",
"cffae78b60b80cd458160b4237ecabadwolflair_cavemechanic.json",
"cffae78b60b80cd458160b4237ecabadwolflair_magicfogmechanics.json",
#Trail In The Hills
"ae33e760ae8ec0e4eb23973391e3b0ad.fog.png",
"ae33e760ae8ec0e4eb23973391e3b0ad.json",
"ae33e760ae8ec0e4eb23973391e3b0adleopardlair_magicfogmechanics.json",
#Tuskgutter's Lair
"10f8ef6f07c72944bbd1178bc2aeb8eb.fog.png",
"10f8ef6f07c72944bbd1178bc2aeb8eb.json",
#The Stag Lord's Fort
"083fa331576e43047b3159d32c3474e5.fog.png",
"083fa331576e43047b3159d32c3474e5.json",
"083fa331576e43047b3159d32c3474e5staglordfort_indoor_emptymechanics.json",
#A Ford Across Skunk River
"40aef0c3aa872bf41b39122a8ffe3f66.fog.png",
"40aef0c3aa872bf41b39122a8ffe3f66.json",
#Overgrown Pool
"69f3a24a26f25874abc7c7278290bcb2.fog.png",
"69f3a24a26f25874abc7c7278290bcb2.json",
#Three-Pine Islet
"3d0f8345470bee24890f4819b85d6f98.fog.png",
"3d0f8345470bee24890f4819b85d6f98.json",
#Tranquil River Bend
"ecbba64703c2cee41a92b9507f85b2bd.fog.png",
"ecbba64703c2cee41a92b9507f85b2bd.json",
"ecbba64703c2cee41a92b9507f85b2bdnormalboggardslairindoor_mechanics.json",
#Ruined Watchtower
"973dacf5a7642a04183f0f10539ce093.fog.png",
"973dacf5a7642a04183f0f10539ce093.json",
"973dacf5a7642a04183f0f10539ce093bigoutdoor_mechanic_ekun.json",
#Bandit Camp
"c966d99c53ae0ef429a64d242946c828.fog.png",
"c966d99c53ae0ef429a64d242946c828.json",
#Sunny Hillock
"33725f60fba56d043acb279ecad2fd25.fog.png",
"33725f60fba56d043acb279ecad2fd25.json",
#Baneful Bog
"b725b040e95e06141b61a0f715801f1b.fog.png",
"b725b040e95e06141b61a0f715801f1b.json",
#Dappled Quagmire
"07535f13f21c273429f985a7a6cdb966.fog.png",
"07535f13f21c273429f985a7a6cdb966.json",
#Hodag Lair
"b73e04776eac5e7499b1dbfd1690f4cd.fog.png",
"b73e04776eac5e7499b1dbfd1690f4cd.json",
#Kobold Camp
"46eeea1eb0d909145ad41108dc9c616f.fog.png",
"46eeea1eb0d909145ad41108dc9c616f.json",
#Monster Den
"a2f0258b8d5bd554ca4ba1526c8e9e1b.fog.png",
"a2f0258b8d5bd554ca4ba1526c8e9e1b.json",
#Lizardfolk Village
"e580965277735c04a91742f9f87f25d6.fog.png",
"e580965277735c04a91742f9f87f25d6.json",
"e580965277735c04a91742f9f87f25d6lizardfolksvillage_childhut_mechanics.json",
"e580965277735c04a91742f9f87f25d6lizardfolksvillage_commonhut_mechanics.json",
"e580965277735c04a91742f9f87f25d6lizardfolksvillage_kingshut_mechanics.json",
#Shrine Of Lamasthu
"a51c0d1b216f7f34eb1c4ceb3c96b860.fog.png",
"a51c0d1b216f7f34eb1c4ceb3c96b860.json",
"a51c0d1b216f7f34eb1c4ceb3c96b860shrineoflamashtu_tsannamechanics.json",
#Empty Skull Rock
"0eb89d7d3670cca49b2e136265b1970c.fog.png",
"0eb89d7d3670cca49b2e136265b1970c.json",
"0eb89d7d3670cca49b2e136265b1970ctrollhoundlair_leftcavemechanic.json",
"0eb89d7d3670cca49b2e136265b1970ctrollhoundlair_rightcavemechanic.json",
#Wolf Lair
"a6e755ca032adb045a3494729cc59c10.fog.png",
"a6e755ca032adb045a3494729cc59c10.json",
#Mud Bowl
"b4c5be9aa65d56547bdd0b949f8e8a02.fog.png",
"b4c5be9aa65d56547bdd0b949f8e8a02.json",
#Bald Stones
"32ff2c708c56b1444a4677ee361e98ec.fog.png",
"32ff2c708c56b1444a4677ee361e98ec.json",
#Ironstone Gully
"26a8cd7adbe016a41a0456c2ffe0031a.fog.png",
"26a8cd7adbe016a41a0456c2ffe0031a.json",
#Kellid Barbarian Camp
"c01a5dc912da3f04bb7898bd958e79d9.fog.png",
"c01a5dc912da3f04bb7898bd958e79d9.json",
#Fey Glade/Trail Of Misfortune Quest
"75be79fe327497d44a0b73ffa9061968.fog.png",
"75be79fe327497d44a0b73ffa9061968.json",
#A Bloody Craft Quest/World Map Encounter
"1274b24ab4b73134ebbb5d588b0c8f0a.fog.png",
"1274b24ab4b73134ebbb5d588b0c8f0a.json",
#Swamp Ruins
"b407f0ee83587a24a8cd37ed7695c848.fog.png",
"b407f0ee83587a24a8cd37ed7695c848.json",
#Goblin Village
"82e9f46e19018e54f81f7cd27dea0e59.fog.png",
"82e9f46e19018e54f81f7cd27dea0e59.json",
#Goblin Fort
"4b90066eae221c747a01997fef7eab0f.fog.png",
"4b90066eae221c747a01997fef7eab0f.json",
#Ancient Mine
"6313d082dd13a9e4f816c41552248e30.fog.png",
"6313d082dd13a9e4f816c41552248e30.json",
#Womb Of lasmasthu
"ab0b15c40826c94489b0bbcba71dc566.fog.png",
"ab0b15c40826c94489b0bbcba71dc566.json",
#Arbor Rock
"d0c56a30c80966047a8f407c0a34ca17.fog.png",
"d0c56a30c80966047a8f407c0a34ca17.json",
"d0c56a30c80966047a8f407c0a34ca17earthelementallair_cavemechanic.json",
#Ratnok Hill
"831d738a0ddb18a46b7a50a2b32fe377.fog.png",
"831d738a0ddb18a46b7a50a2b32fe377.json",
"831d738a0ddb18a46b7a50a2b32fe377hiddeneven3_cr_wereratlair_indoor_mechanics.json",
#Saint Galvan's Gullet
"61fe89577c6db304a82a21a000f26b6a.fog.png",
"61fe89577c6db304a82a21a000f26b6a.json",
#Tenebrous 1-3
"430414f71b8a36444913d13ebd61b6df.fog.png",
"430414f71b8a36444913d13ebd61b6df.json",
"89c6ff323b9b82c4598689f541d27cf9.fog.png",
"89c6ff323b9b82c4598689f541d27cf9.json",
"e93a92deab159b94e9562e9d17edd9ba.fog.png",
"e93a92deab159b94e9562e9d17edd9ba.json",
#Tenebrous 5-7
"a45202084ee138b4ebff83bb72e6de09.fog.png",
"a45202084ee138b4ebff83bb72e6de09.json",
"c8013f5bce7062540953dbe8fcce2d45.fog.png",
"c8013f5bce7062540953dbe8fcce2d45.json",
"eff8d5d34bbdc774a83a99db8d37df72.fog.png",
"eff8d5d34bbdc774a83a99db8d37df72.json",
#Bald Hilltop
"18ac371fab4e6274faeb4d6b6ddaf858.fog.png",
"18ac371fab4e6274faeb4d6b6ddaf858.json",
"18ac371fab4e6274faeb4d6b6ddaf858bloodmoonportal_mechanicstieri.json"
"18ac371fab4e6274faeb4d6b6ddaf858bloodmoonportal_mechanicstierii.json"
"18ac371fab4e6274faeb4d6b6ddaf858bloodmoonportal_mechanicstieriii.json",
"18ac371fab4e6274faeb4d6b6ddaf858bloodmoonportal_mechanicstieriv.json",
"18ac371fab4e6274faeb4d6b6ddaf858bloodmoonportal_mechanicstierv.json",
"18ac371fab4e6274faeb4d6b6ddaf858bloodmoonportal_mechanicstiervi.json"
#poachers hideout
"6d216c21d3dc70d4a87f646a9a3dd4b7.fog.png",
"6d216c21d3dc70d4a87f646a9a3dd4b7.json",
#world map encounter
"b09b269c711ddc243b254a5ea0e5c666.fog.png",
"b09b269c711ddc243b254a5ea0e5c666.json",
#Technic League Hideout
#"b5e10be5d85d7234ab82708422a5faab.fog.png",
#"b5e10be5d85d7234ab82708422a5faab.json",
#Inconsequent Debates
"07a63b7be5ccc3d468e80d80dfdac473.fog.png",
"07a63b7be5ccc3d468e80d80dfdac473.json",
#Adamantine Shield Fortress
"b0828e5f11f72474d9b37340a6a2b15f.fog.png",
"b0828e5f11f72474d9b37340a6a2b15f.json",
#Honour And Duty World Encounter
"687a79a44abb7e64981001d5a195e6a0.fog.png",
"687a79a44abb7e64981001d5a195e6a0.json",
#Bridge Over Gudrun River
"d3de7887f51da7f499c73cd8173f8f79.fog.png",
"d3de7887f51da7f499c73cd8173f8f79.json",
"d3de7887f51da7f499c73cd8173f8f79bigkamelandsoutdoor_cave_mechanics.json",
"d3de7887f51da7f499c73cd8173f8f79bigkamelandsoutdoor_withgoblinsandbandits.json",
#Warld Map Event
"35e1655f9acb0f948a7fa1b098e0e903.fog.png",
"35e1655f9acb0f948a7fa1b098e0e903.json",
#Overgrown Cavern
"6cbf7bd9e8b0eee46831a7b4ff90f697.fog.png",
"6cbf7bd9e8b0eee46831a7b4ff90f697.json",
"6cbf7bd9e8b0eee46831a7b4ff90f697c31_oldcavedungeon_mechanics.json",
#Precipice Trail
"1149a6b7238c8934295e20b418ed334c.fog.png",
"1149a6b7238c8934295e20b418ed334c.json",
"1149a6b7238c8934295e20b418ed334cathachlaircave_mechanic.json",
#Ghost Stone
"d2ea3757141901b4fa334575248dec38.fog.png",
"d2ea3757141901b4fa334575248dec38.json",
#Little Selen Source
"000eb3073c80b164985201382be3a038.fog.png",
"000eb3073c80b164985201382be3a038.json",
#World Map Encounter
"a025f724bfbfee745ab08e2c7577af7b.fog.png",
"a025f724bfbfee745ab08e2c7577af7b.json",
#Rotten Cave/Crooked Teeth
"019292805db2bb146a3d3dec1ad3fbf1.fog.png",
"019292805db2bb146a3d3dec1ad3fbf1.json",
"329f61598cd16694d851cef9b73992d3.fog.png",
"329f61598cd16694d851cef9b73992d3.json",
"329f61598cd16694d851cef9b73992d3shumblingmoundlaircave01_mechanic.json",
"329f61598cd16694d851cef9b73992d3shumblingmoundlaircave02_mechanic.json",
"c4fcfbfec4360a0468524ae66839a46d.fog.png",
"c4fcfbfec4360a0468524ae66839a46d.json",
"c4fcfbfec4360a0468524ae66839a46dshumblingmoundlairfwcave_mechanic.json",
"c9caf9417e98b554882057a87ffc450d.fog.png",
"c9caf9417e98b554882057a87ffc450d.json",
#World Encounter/Barbarians
"c4b40aaba21c41244bc0678c8e9d0885.fog.png",
"c4b40aaba21c41244bc0678c8e9d0885.json"
#Rinderpest Burial Grounds
"4986dd6e31edbac409b9545eddcc4fee.fog.png",
"4986dd6e31edbac409b9545eddcc4fee.json",
#Spider Lair
"c34454f9b2b524c438574db0a9adc8aa.fog.png",
"c34454f9b2b524c438574db0a9adc8aa.json",
#Unfinished Clearing
"596c49b6e9385e04a85729cdf297d16f.fog.png",
"596c49b6e9385e04a85729cdf297d16f.json",
"596c49b6e9385e04a85729cdf297d16fworglaircave_mechanic.json"
#Blood Furrows
"732a8d58d72f301459ffc5e00b355ff9.fog.png",
"732a8d58d72f301459ffc5e00b355ff9.json",
#City Of Hollow Eyes
#"63f0934aa847a88408da0b04d933669d.fog.png",
#"63f0934aa847a88408da0b04d933669d.json",
#"7aa49505621355448931f8e69b74d1a9.fog.png",
#"7aa49505621355448931f8e69b74d1a9.json",
#Sepulcher of Forgotten Heroes
"0680f2397d9a12c43bf0cc9fe2c25679.fog.png",
"0680f2397d9a12c43bf0cc9fe2c25679.json",
#Collapsed Passage
"411e8dcf2ad010f44a52ba9b9ee12b79.fog.png",
"411e8dcf2ad010f44a52ba9b9ee12b79.json",
#Linnorm's Grave
"51b0aa4ff2b705543a2b6c541bd9198a.fog.png",
"51b0aa4ff2b705543a2b6c541bd9198a.json",
#Shievering Glade
"f8b1746f525ce7341bc41d0fb7701e94.fog.png",
"f8b1746f525ce7341bc41d0fb7701e94.json",
#World Map / Raven Dialog
"f6a009b8113efc64d9fc561daa68a11f.fog.png",
"f6a009b8113efc64d9fc561daa68a11f.json",
#Vordakai
"0ec59b25ded041d43a9399768db58ca6.fog.png",
"0ec59b25ded041d43a9399768db58ca6.json",
"2b88c6b8e3d799b47a330786b25facc3.fog.png",
"2b88c6b8e3d799b47a330786b25facc3.json",
"465346f31162c444ba7b3e8292735666.fog.png",
"465346f31162c444ba7b3e8292735666.json",
"b4789ad28d5ae9340bf4ea2ed747a8b0.fog.png",
"b4789ad28d5ae9340bf4ea2ed747a8b0.json",
#Country Road
"8a5d04cb619b6944484795d6169c05b9.fog.png",
"8a5d04cb619b6944484795d6169c05b9.json",
#Flintrock Grassland
"609170613556500419cc6e051db1dc0a.fog.png",
"609170613556500419cc6e051db1dc0a.json",
"609170613556500419cc6e051db1dc0abrevoyborderlandsoutdoorbattle_mechanics2.json",
#Raspberry Gully
"839920f27edd9504fa461bc228ed1249.fog.png",
"839920f27edd9504fa461bc228ed1249.json",
#Fossil Field
"0a365075a315a214e896d611df25a3a8.fog.png",
"0a365075a315a214e896d611df25a3a8.json",
#Southern Barrens
"ae47b5845e441174cabdd33a443497f1.fog.png",
"ae47b5845e441174cabdd33a443497f1.json",
#Six Bears Camp
"abe22ee34c167854eace91742ca32a85.fog.png",
"abe22ee34c167854eace91742ca32a85.json",
"abe22ee34c167854eace91742ca32a85sixbearscamp_amiriq3_mechanics.json",
#Wicked Field
"aef1745e8077e9d46bfa26422f8fb782.fog.png",
"aef1745e8077e9d46bfa26422f8fb782.json",
#Giant's Palm
"1da7f2437df3e694d8bafff771900376.fog.png",
"1da7f2437df3e694d8bafff771900376.json",
#Gnawed Rocks
"412768f665a5bf14297fcc3ec46efa8e.fog.png",
"412768f665a5bf14297fcc3ec46efa8e.json",
#World Map Encounter
"35e1655f9acb0f948a7fa1b098e0e903.fog.png",
"35e1655f9acb0f948a7fa1b098e0e903.json",
#Two-Faced Hill
"93208bd1490e0444d90355237a7c6837.fog.png",
"93208bd1490e0444d90355237a7c6837.json",
"93208bd1490e0444d90355237a7c6837werewolflaircave_mechanic.json",
#Charred Ruins
"97fc0d0737d629744a4141d7b5501598.fog.png",
"97fc0d0737d629744a4141d7b5501598.json",
#Serpent Trail
"652b64dbf9509d14a8376e3394394562.fog.png",
"652b64dbf9509d14a8376e3394394562.json",
"c6b7bd4e20012b54cbe5643a815d20a3.fog.png",
"c6b7bd4e20012b54cbe5643a815d20a3.json",
#Desecrated Cairn
"c89ab7c45ba50e44890c38230a78c6c3.fog.png",
"c89ab7c45ba50e44890c38230a78c6c3.json",
#Tenebrous depth 9-11
"387b37e9b83c3c74788ff92c61acf891.fog.png",
"387b37e9b83c3c74788ff92c61acf891.json",
"db654eeff2c644f4c8532d57871261bb.fog.png",
"db654eeff2c644f4c8532d57871261bb.json",
"ffba39a87ea3efe4385db8fe42339c35.fog.png",
"ffba39a87ea3efe4385db8fe42339c35.json",
#Tenebrous depth 13-15
"11ca258805046934fb9fd93b9ab5330d.fog.png",
"11ca258805046934fb9fd93b9ab5330d.json",
"229f21a095945db42965220c3e40434c.fog.png",
"229f21a095945db42965220c3e40434c.json",
"d45700eb0e52784498d36c18bc015304.fog.png",
"d45700eb0e52784498d36c18bc015304.json",
#Armags Tomb
"4777ca570ca58c248a679ec3e9d9335d.fog.png",
"4777ca570ca58c248a679ec3e9d9335d.json",
"f0e41714d8f2bc14bb604bc0d4cfe40d.fog.png",
"f0e41714d8f2bc14bb604bc0d4cfe40d.json",
"f0e41714d8f2bc14bb604bc0d4cfe40darmagstomb_level1_mechanics.json",
"f0e41714d8f2bc14bb604bc0d4cfe40darmagstombafter01_mechanics.json",
"f0e41714d8f2bc14bb604bc0d4cfe40darmagstombbefore_mechanics.json",
#Temple Of Shelyn
"6fb9e1a5091009249a62ce80ce7a74a6.fog.png",
"6fb9e1a5091009249a62ce80ce7a74a6.json",
#Deal With The Devil/Secluded Lodge
"be20f85c98cc8eb4fa15b0ba6bd5f205.fog.png",
"be20f85c98cc8eb4fa15b0ba6bd5f205.json",
#Brineheart
"f5f65d14f9637cb4e9977a8440d8ad71.fog.png",
"f5f65d14f9637cb4e9977a8440d8ad71.json",
"f5f65d14f9637cb4e9977a8440d8ad71brineheart_mechanics.json",
#Cave From Luna's Map
"99ca8640180f8314e98afcdd222c6213.json",
#Lost Dwarfen Fortress - revisit (no problem if the file was deleted after 1st visit)
"44480778d16912c4fb783a91605bb319.fog.png",
"44480778d16912c4fb783a91605bb319.json",
"b0828e5f11f72474d9b37340a6a2b15f.fog.png",
"b0828e5f11f72474d9b37340a6a2b15f.json",
#Sharp Fangs Tribal Camp/Rag Quest
"3222bc64678205541aeea78f13dd4d7f.fog.png",
"3222bc64678205541aeea78f13dd4d7f.json",
#Wicked Hill
"ae69121c724efa742950fe78d93fa0df.fog.png",
"ae69121c724efa742950fe78d93fa0df.json",
#Ilthuliaks Lair
"a0faae001decd1544b31d6451a8f2ddd.fog.png",
"a0faae001decd1544b31d6451a8f2ddd.json",
"a0faae001decd1544b31d6451a8f2dddillthuliaklairindoorempty_mechanics.json",
#Carnival Glade
"21d4ffd9eb813ef4a86e44830dac172d.fog.png",
"21d4ffd9eb813ef4a86e44830dac172d.json",
"dc2a2dcb3b1b5c1499a6235425bfc469.fog.png",
"dc2a2dcb3b1b5c1499a6235425bfc469.json",
#Rill-And-Spill
"191d887bce4c23743b65acd366f53199.fog.png",
"191d887bce4c23743b65acd366f53199.json",
"50882ae3f8bc11e4e97eb8df17f16184.fog.png",
"50882ae3f8bc11e4e97eb8df17f16184.json",
#Ornate Ruins
"2353cebfb4be55f4f9d9882dd0fbbe54.fog.png",
"2353cebfb4be55f4f9d9882dd0fbbe54.json",
#Rushlight Fields
"2272c3a38214c1b4da85887f41001757.fog.png",
"2272c3a38214c1b4da85887f41001757.json",
"2272c3a38214c1b4da85887f41001757rushlightfestivalcamp_irovettitent_mechanics.json",
#Weeping Grove
"2e15db38eeedd3a43b1eeb6bd8587380.fog.png",
"2e15db38eeedd3a43b1eeb6bd8587380.json",
#Forest Ballroom
"585a85f969d2c3644ac69283958981e7.fog.png",
"585a85f969d2c3644ac69283958981e7.json",
#Giggling Hill
"cfddda7a7cacd614d987037c9aaede5f.fog.png",
"cfddda7a7cacd614d987037c9aaede5f.json",
"cfddda7a7cacd614d987037c9aaede5fredcaplaircavefw_mechanics.json",
#Pitax River Bend
"bcb96e580e0ec6e4b888a1428069ddde.fog.png",
"bcb96e580e0ec6e4b888a1428069ddde.json",
#River Blades' Camp
"a5b1798c2c0ceca4cb5c05af009bc54c.fog.png",
"a5b1798c2c0ceca4cb5c05af009bc54c.json",
#Littletown
"f2c0665786c0fc142b8d6668e31fb3e1.fog.png",
"f2c0665786c0fc142b8d6668e31fb3e1.json",
"f2c0665786c0fc142b8d6668e31fb3e1littletowntavern_mechanics.json",
#The Menagerie
"8e51b001b281ad845b8f09c9cd31e810.fog.png",
"8e51b001b281ad845b8f09c9cd31e810.json",
#Elven Camp
"934343f476333594abc35834527a3824.fog.png",
"934343f476333594abc35834527a3824.json",
#Whiterose Abbey
"5ec616b225074e246a6f64b3554819fb.fog.png",
"5ec616b225074e246a6f64b3554819fb.json",
#Goblin Merchant
"0b5903c0adec15d47b3809d1d1e5a871.fog.png",
"0b5903c0adec15d47b3809d1d1e5a871.json",
#Middle Of Nowhere
"7e0929687b62faf46b1997f38e924650.fog.png",
"7e0929687b62faf46b1997f38e924650.json",
"f2bfb961a0ca835438669c556a145c3f.fog.png",
"f2bfb961a0ca835438669c556a145c3f.json",
#Pitax
"87eb9e17e4d796741960c48b0226e124.fog.png",
"87eb9e17e4d796741960c48b0226e124.json",
"87eb9e17e4d796741960c48b0226e124c51-linziq3_pitax.json",
"87eb9e17e4d796741960c48b0226e124pitax_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtown_academy_battlestate_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtown_battlestate_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtown_port_battlestate_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtown_riversjustice_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtownacademy_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtownport_mechanics.json",
"87eb9e17e4d796741960c48b0226e124pitaxtowntavern_mechanics.json",
"9df00192e3a3ab642a16290c588ad5d6.fog.png",
"9df00192e3a3ab642a16290c588ad5d6.json",
"bf9dbc2998849ee40bbdba9cb40a7d4c.fog.png",
"bf9dbc2998849ee40bbdba9cb40a7d4c.json",
"bf9dbc2998849ee40bbdba9cb40a7d4cirovettipalace_mechanics_dlc2mimics.json",
"bf9dbc2998849ee40bbdba9cb40a7d4cirovettipalacecellar_emptymechanics.json",
"bf9dbc2998849ee40bbdba9cb40a7d4cirovettipalacechamber_emptymechanics.json",
#Druid's Refuge
"fdbc9446c58bdc64eba6d7d84b095798.fog.png",
"fdbc9446c58bdc64eba6d7d84b095798.json",
#Grocery Stalls
"3b0a1c6202229c34a8a66073a694c8f6.fog.png",
"3b0a1c6202229c34a8a66073a694c8f6.json",
"3bfe9d145dbb8e541b3113e2ae339ca3.fog.png",
"3bfe9d145dbb8e541b3113e2ae339ca3.json",
"3bfe9d145dbb8e541b3113e2ae339ca3mandragoralaircave_mechanics.json",
#Castle Of Knives
"4b335fbba8e7ee34cb01cf5ad704e0ff.fog.png",
"4b335fbba8e7ee34cb01cf5ad704e0ff.json"
]

zout = zipfile.ZipFile (save_name, "w")
for item in save_zip.infolist():
    buffer = save_zip.read(item.filename)
    if (item.filename not in removable):
        print("preserve " + item.filename)
        zout.writestr(item, buffer)
    else:
        print("remove " + item.filename)
zout.close()
save_zip.close()

