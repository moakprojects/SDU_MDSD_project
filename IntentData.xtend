package org.xtext.project.generator

import org.eclipse.xtend.lib.annotations.Data
import java.util.List

@Data class IntentData {
	List<String> training_phrases
    List<String> messages
	
	def getIntentAsArray() {
		#[training_phrases.convertToString, messages.convertToString]
	}
	
	def convertToString(List<String> list) {
		list.map[li | "'" + li + "'"]
	}
	
	def convertToString(String string) {
		"'" + string + "'"
	}
}