package au.edu.monash.mes.envimet;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.TreeMap;

/*
 The data files (.EDT) are simple binary files of type "float" with a single precision.

 The file are written with the following loop logic

 For z:= 0 to ZZ
 For y:=1 to YY
 For x:=1 to XX
 {
 Write Value[x][y][z]
 }

 with XX,YY and ZZ being the dimensions of the model domain. 
 */

public class ReadEDTFile
{

	private TreeMap data;

	public TreeMap getData()
	{
		return data;
	}

	public void setData(TreeMap data)
	{
		this.data = data;
	}

	public ReadEDTFile(String filename, ReadEDIFile readEDIFile)
	{
		super();
		readEDTFile(filename, readEDIFile);
	}

	public void readEDTFile(String filename, ReadEDIFile readEDIFile)
	{
		File file = new File(filename);
		FileInputStream fis = null;
		BufferedInputStream bis = null;
		DataInputStream dis = null;

		data = new TreeMap<String, ArrayList>();
		ArrayList<String> fileVariables = readEDIFile.getFileVariables();

		try
		{
			fis = new FileInputStream(file);
			bis = new BufferedInputStream(fis);
			dis = new DataInputStream(bis);

			for (int i = 0; i < readEDIFile.getNumOfVariablesInFile(); i++)
			{
				ArrayList variableData = new ArrayList<Float>();
				String variableName = fileVariables.get(i);

				for (int z = 0; z < readEDIFile.getNumOfZGrids(); z++)
				{
					for (int y = 1; y < readEDIFile.getNumOfXGrids(); y++)
					{
						for (int x = 1; x < readEDIFile.getNumOfXGrids(); x++)
						{
							Float floatData = dis.readFloat();
							variableData.add(floatData);
						}
					}
				}				
				data.put(variableName, variableData);
			}

			// dispose all the resources after using them.
			fis.close();
			bis.close();
			dis.close();

		} catch (FileNotFoundException e)
		{
			e.printStackTrace();
		} catch (IOException e)
		{
			e.printStackTrace();
		}
	}

}
