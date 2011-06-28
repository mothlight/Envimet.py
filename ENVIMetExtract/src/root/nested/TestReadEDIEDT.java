package au.edu.monash.mes.envimet;

import java.util.ArrayList;
import java.util.TreeMap;

public class TestReadEDIEDT {

	public static void main(String[] args) {
		
		String filename = "/home/nice/.wine/drive_c/ENVImetprojects/Monash/Test/surface/MySim_FX_09.00.00 23.06.2010";
		String ediFileType = ".EDI";
		String edtFileType = ".EDT";
		
		ReadEDIFile readEDI = new ReadEDIFile(filename + ediFileType);
		
		ArrayList<String> fileVariables = readEDI.getFileVariables();
		
		System.out.println("File contents");
						
		System.out.println(readEDI.getTitleOfSim());
		System.out.println(readEDI.getNumOfXGrids());
		System.out.println(readEDI.getNumOfYGrids());
		System.out.println(readEDI.getNumOfZGrids());
		System.out.println(readEDI.getNumOfVariablesInFile());
		System.out.println(fileVariables);
		
		System.out.println(readEDI.getGridSpacingX());
		System.out.println(readEDI.getGridSpacingY());
		System.out.println(readEDI.getGridSpacingZ());
		
		ReadEDTFile readEDTFile = new ReadEDTFile(filename + edtFileType, readEDI);
		
		TreeMap<String, ArrayList> edtData = readEDTFile.getData();
		
		for (int i=0;i<fileVariables.size();i++)
		{
			String variable = fileVariables.get(i);			
			ArrayList variableData = edtData.get(variable);			
			System.out.println(variable + "=" + variableData);
		}
		
	}

}
