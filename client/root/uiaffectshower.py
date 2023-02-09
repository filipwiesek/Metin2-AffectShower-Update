## find:
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		[...]
			self.__ArrangeImageList()

## replace with:
	def BINARY_NEW_AddAffect(self, type, pointIdx, value, duration):
		[...]
			if not app.ENABLE_AFFECT_FIX:
				self.__ArrangeImageList()

## find:
	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		[...]
		self.__ArrangeImageList()

## replace with:
	def BINARY_NEW_RemoveAffect(self, type, pointIdx):
		[...]
		if not app.ENABLE_AFFECT_FIX:
			self.__ArrangeImageList()

## paste below:
	if app.ENABLE_AFFECT_FIX:
		def BINARY_NEW_RefreshAffect(self):
			self.__ArrangeImageList()

## find:
class AffectImage(ui.ExpandedImageBox):
	[...]

## replace with:
class AffectImage(ui.ExpandedImageBox):

	def __init__(self):
		ui.ExpandedImageBox.__init__(self)

		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.HideToolTip()

		self.isSkillAffect = True
		self.description = None
		self.endTime = 0
		self.affect = None
		self.isClocked = True

	def SetAffect(self, affect):
		self.affect = affect

	def GetAffect(self):
		return self.affect

	def FormatTime(self, time):
		text = ""

		d = time // (24 * 3600)
		time = time % (24 * 3600)
		h = time // 3600
		time %= 3600
		m = time // 60
		time %= 60
		s = time

		if d:
			text += "%dd " % d
		if text or h:
			text += "%dg " % h
		if text or m:
			text += "%dm " % m
		if text or s:
			text += "%ds " % s

		return text[:-1]

	def SetToolTipText(self, text, x = 0, y = -19):
		self.toolTip.ClearToolTip()
		self.toolTip.AppendSpace(-5)
		self.toolTip.AppendDescription(text, 26)

	def SetDescription(self, description):
		self.description = description
		self.__UpdateDescription2()

	def SetDuration(self, duration):
		self.endTime = 0
		if duration > 0:
			self.endTime = app.GetGlobalTimeStamp() + duration
			leftTime = self.FormatTime(self.endTime - app.GetGlobalTimeStamp())
			self.toolTip.AppendTextLine("(%s : %s)" % (localeInfo.LEFT_TIME, leftTime))
			self.toolTip.ResizeToolTip()

	def UpdateAutoPotionDescription(self):
		potionType = player.AUTO_POTION_TYPE_HP if self.affect == chr.NEW_AFFECT_AUTO_HP_RECOVERY\
			else player.AUTO_POTION_TYPE_SP
		isActivated, currentAmount, totalAmount, slotIndex = player.GetAutoPotionInfo(potionType)

		try:
			amountPercent = (float(currentAmount) / totalAmount) * 100.0
		except:
			amountPercent = 100.0

		self.toolTip.childrenList[-1].SetText(self.description % amountPercent)

	def SetClock(self, isClocked):
		self.isClocked = isClocked
		self.SetDescription(self.description)
		
	def UpdateDescription(self):
		if not self.isClocked:
			return
	
		if not self.description:
			return
			
		if self.endTime > 0:
			leftTime = self.FormatTime(self.endTime - app.GetGlobalTimeStamp())

			self.toolTip.childrenList[-1].SetText("(%s : %s)" % (localeInfo.LEFT_TIME, leftTime))

	def __UpdateDescription2(self):
		if not self.description:
			return

		toolTip = self.description
		self.SetToolTipText(toolTip, 0, 40)

	def SetSkillAffectFlag(self, flag):
		self.isSkillAffect = flag

	def IsSkillAffect(self):
		return self.isSkillAffect

	def OnMouseOverIn(self):
		self.toolTip.ShowToolTip()

	def OnMouseOverOut(self):
		self.toolTip.HideToolTip()

## find:
	def __ArrangeImageList(self):
		[...]

## replace with:
	def __ArrangeImageList(self):
		xPos = 0
		yPos = 0

		xMax = 0

		countRow = 0

		if self.lovePointImage:
			if self.lovePointImage.IsShow():
				self.lovePointImage.SetPosition(xPos, yPos)
				xPos += self.IMAGE_STEP
				countRow += 1

		if self.horseImage:
			self.horseImage.SetPosition(xPos, yPos)
			xPos += self.IMAGE_STEP
			countRow += 1

		for image in self.affectImageDict.values():
			image.SetPosition(xPos, yPos)
			xPos += self.IMAGE_STEP
			countRow += 1

			if xMax < xPos:
				xMax = xPos

			if countRow == 10:
				xPos = 0
				yPos += self.IMAGE_STEP
				countRow = 0

		self.SetSize(xMax, yPos + 26)
