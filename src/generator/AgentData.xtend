package org.xtext.project.generator

import org.eclipse.xtend.lib.annotations.Data
import java.util.List

@Data class AgentData {
	String parent
	String displayName
	String language
	String timeZone
	
	def getAgentAsArray() {
		#[parent.convertToString, displayName.convertToString, language.convertToString, timeZone.convertToString]
	}
	
	def convertToString(String string) {
		"'" + string + "'"
	}
}
